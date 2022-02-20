import vk_api, random, time, os, vk_captchasolver as vc



yes = 0
while True:
    time.sleep(30)
    yes +=1
    if yes == 12:
        yes = 1
    try:
        vk_session = vk_api.VkApi(token='8aeca9c1696fced0f6073afb4e26f4b7f89e65c2ea29e0b6018e855e0dd5e98f606ad63e57a5afd345ad1')
        vk_apii = vk_session.get_api()
        upload = vk_api.VkUpload(vk_apii)
        upload.photo_profile(photo=f"{yes}.jpg")
    except vk_api.Captcha:
        cycle = True
        while cycle:
            try:
                upload.photo_profile(photo=f"{yes}.jpg")
            except vk_api.Captcha as cptch:
                result_solve_captcha = vc.solve(sid=int(cptch.sid), s=1)
                try:
                    cptch.try_again(result_solve_captcha)
                    cycle = False
                except vk_api.Captcha as cptch2:
                    pass
            except:
                pass
    except:
        pass

