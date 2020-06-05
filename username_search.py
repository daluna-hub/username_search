import colorama, requests
from colorama import Fore


def usrchk(usernamee):
    
    try: #=====================
        try: #                 \
            try: #              ====== I'm lazy about tabs, that code come from one of my programs.
                try: #         /
                    try: #=====
                        try:
                            porn = ('['+Fore.MAGENTA+'PORN'+Fore.RESET+']')
                            forum = ('['+Fore.YELLOW+'FORUM'+Fore.RESET+']')
                            gore = ('['+Fore.RED+'GORE'+Fore.RESET+']')
                            meet = ('['+Fore.MAGENTA+'MEETING <3'+Fore.RESET+']')
                            fitness = ('['+Fore.BLUE+'FITNESS / SPORT'+Fore.RESET+']')
                            hacking = ('['+Fore.CYAN+'HACKING'+Fore.RESET+']')
                            live = ('['+Fore.GREEN+'BROADCAST'+Fore.RESET+']')
                            social = ('['+Fore.BLUE+'SOCIAL'+Fore.RESET+']')
                            gaming = ('['+Fore.GREEN+'GAMING'+Fore.RESET+']')
                            shop = ('['+Fore.GREEN+"$"+Fore.YELLOW+' MONEY / SHOP '+Fore.GREEN+"$"+Fore.RESET+']')
                            voyage = ('['+Fore.MAGENTA+'TRAV'+Fore.YELLOW+'ELING'+Fore.RESET+']')
                            music = ('['+Fore.GREEN+' "*-_ MUSIC _-*"'+Fore.RESET+']')

                            result_count = []
                            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'}
                            try:
                                url = f"http://www.jeuxvideo.com/profil/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{forum} [jeuxvideo.com] {url}")
                                    result_count.append('.')
                            except:
                                except_print()
                                pass
                            try:
                                url = (f"http://kik.me/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    if  ('<h1 class="display-name"> </h1>') in r.text:
                                        pass
                                    else:
                                        print(f"{social} [kik.me] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.flickr.com/photos/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    print(f"{social} [flickr] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.pinterest.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    print(f"{social} [pinterest] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://soundcloud.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    print(f"{music} [soundcloud] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.buzzfeed.com/{usernamee}")
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" or "302" in re:
                                    print(f"{forum} [Buzzfeed] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.wechall.net/profile/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if "<li>The User is unknown.</li>" in r.text:
                                        pass
                                    else:
                                        print(f"{hacking} [wechall.net] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://en.wikipedia.org/wiki/User:{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200":
                                    print(f"{forum} [Wikipedia] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://pornhub.com/users/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200":
                                    print(f"{porn} [Pornhub] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://cash.app/${usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    print(f"{shop} [cash.app] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://disqus.com/by/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [disqus] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.xvideos.com/channels/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    print(f"{porn} [xVideos] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://badoo.com/profile/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{meet} [Badoo] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://ello.co/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    print(f"{social} [ello] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://venmo.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    print(f"{shop} [Venmo] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.artstation.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    print(f"{social} [artstation] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.reddit.com/user/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re or "500":
                                    print(f"{social} [reddit] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.patreon.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{shop} [patreon] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.deviantart.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{forum} [DeviantArt] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://500px.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [500px] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.gotinder.com/@{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    if ("deeplink_error" in r.text):
                                        pass
                                else:
                                        print(f"{meet} [Tinder] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://vk.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [vk.com] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://about.me/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"[about.me] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://t.me/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    if "tgme_icon_user" in r.text:
                                        pass
                                    else:
                                        print(f"{social} [Telegram] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://m.twitch.tv/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{live} [Twitch] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://myspace.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [MySpace] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.youtube.com/user/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [YouTube] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.facebook.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [Facebook] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.instagram.com/{usernamee}")
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [Instagram] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.tripadvisor.co.uk/Profile/{usernamee}")
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{voyage} [tripadvisor] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://smg.photobucket.com/user/{usernamee}/library")
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [Photobucket] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://steamcommunity.com/id/{usernamee}")
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    if "error_ctn" in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [Steam] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.last.fm/user/{usernamee}")
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    if "not found" in r.text:
                                        pass
                                    else:
                                        print(f"{social} [LastFM] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.ebay.com/usr/{usernamee}")
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    if "not found" in r.text:
                                        pass
                                    else:
                                        print(f"{shop} [Ebay] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.etsy.com/people/{usernamee}")
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{shop} [Etsy] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = (f"https://www.myfitnesspal.com/user/" + usernamee+ "/status")
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{fitness} [MyFitnessPal] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://vimeo.com/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [Vimeo] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.kaotic.com/user/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gore} [Kaotic] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.behance.net/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [Behance] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://gitlab.com/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [Gitlab] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://github.com/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [Github] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://fhtracker.com/profile/xbox/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if "We could not find your stats, please ensure your platform and name are correct" in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [FOR HONOR XBOX] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://rocketr.net/sellers/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200":
                                    print(f"{shop} [Rocketr] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://fhtracker.com/profile/pc/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if "We could not find your stats, please ensure your platform and name are correct" in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [FOR HONOR PC] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://fhtracker.com/profile/psn/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if "We could not find your stats, please ensure your platform and name are correct" in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [FOR HONOR PS4] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://fortnitetracker.com/profile/touch/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if "To avoid grouped matches, leave this page open in your browser or mobile app while playing." not in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [Fortnite] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://{usernamee}.selly.store"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{shop} [Selly] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.bestgore.com/members/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gore} [BestGore] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://codstats.net/profile/xbox/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gaming} [COD WARZONE XBOX] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://codstats.net/profile/pc/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gaming} [COD WARZONE PC] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.tipeeestream.com/{usernamee}/donation"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re or "302" in re:
                                    print(f"{shop} [Tipeee] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://codstats.net/profile/ps4/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gaming} [COD WARZONE PS4] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://r6.tracker.network/profile/xbox/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gaming} [R6 XBOX] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://r6.tracker.network/profile/psn/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gaming} [R6 PS4] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://r6.tracker.network/profile/pc/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gaming} [R6 PC] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://streamlabs.com/{usernamee}/tip"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re or "302" in re:
                                    print(f"{shop} [streamlabs] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://tracker.gg/apex/profile/xbl/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gaming} [APEX LEGEND XBOX] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://rocketleague.tracker.network/profile/xbox/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if 'We could not find your stats, please ensure your platform and name are correct' in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [ROCKET LEAGUE XBOX] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://fr.tipeee.com/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re or "302" in re:
                                    print(f"{shop} [Tipeee] {url}")
                                    result_count.append('.')					
                            except:
                                pass
                            try:
                                url = f"https://fr.gravatar.com/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"[Gravatar] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://openclassrooms.com/fr/membres/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{forum} [openclassrooms] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://rocketleague.tracker.network/profile/ps/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if 'We could not find your stats, please ensure your platform and name are correct' in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [ROCKET LEAGUE PS4] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://venmo.com/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{shop} [Venmo] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://rocketleague.tracker.network/profile/steam/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if 'We could not find your stats, please ensure your platform and name are correct' in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [ROCKET LEAGUE STEAM] {url}")
                                        result_count.append('.')
                                total_accounts = str(len(result_count))
                            except:
                                pass
                            try:
                                url = f"https://battlefieldtracker.com/bfv/profile/xbl/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if 'We could not find your stats, please ensure your platform and name are correct' in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [BATTLEFIELD XBOX] {url}")
                                        result_count.append('.')
                                total_accounts = str(len(result_count))
                            except:
                                pass
                            try:
                                url = f"https://battlefieldtracker.com/bfv/profile/psn/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if 'We could not find your stats, please ensure your platform and name are correct' in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [[BATTLEFIELD PS4] {url}")
                                        result_count.append('.')
                                total_accounts = str(len(result_count))
                            except:
                                pass
                            try:
                                url = f"https://battlefieldtracker.com/bfv/profile/origin/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    if 'We could not find your stats, please ensure your platform and name are correct' in r.text:
                                        pass
                                    else:
                                        print(f"{gaming} [BATTLEFIELD PC] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.bestgore.com/author/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gore} [BestGore] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.periscope.tv/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{live} [Periscope] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.xboxgamertag.com/search/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{gaming} [XBOX] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://cams.com/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{porn} [Cams.com] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://cracked.to/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    if '<span class="active"><span>404 Error</span></span>' in r.text:
                                        pass
                                    else:
                                        print(f"{hacking} [Cracked.to] {url}")
                                        result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://hackaday.com/author/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{hacking} [Hackaday] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.cam4.fr/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{porn} [Cam4] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.instant-gaming.com/fr/user/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re or "302" in re:
                                    print(f"{gaming} [instant-gaming] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://raidforums.com/User-{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{hacking} [RaidForums] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.pillowfort.social/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [PillowFort] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://fr.xhamster.com/users/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{porn} [xHamster] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://{usernamee}.tumblr.com/"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{social} [Tumblr] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.xnxx.com/porn-maker/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{porn} [xnxx] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.utip.io/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re or "302" in re:
                                    print(f"{shop} [uTip] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.root-me.org/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{hacking} [root-me] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://journaldesfemmes.com/profile/user/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{forum} [journaldesfemmes] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"http://mon.psychologies.com/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{forum} [mon.psychologies.com] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.kickstarter.com/profile/{usernamee}"
                                r = requests.get(url,headers=headers,allow_redirects=False)
                                re = str(r.status_code)
                                if "404" in re or "302" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{shop} [kickstarter] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://www.growthhacking.fr/u/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{hacking} [growthhacking.fr] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"https://fr.redtube.com/users/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{porn} [Redtube] {url}")
                                    result_count.append('.')
                            except:
                                pass
                            try:
                                url = f"http://club.caradisiac.com/{usernamee}"
                                r = requests.get(url,headers=headers)
                                re = str(r.status_code)
                                if "404" in re:
                                    pass
                                elif "200" in re:
                                    print(f"{forum} [Caradisiac] {url}")
                                    result_count.append('.')
                            except:
                                pass
        
                            total_accounts = str(len(result_count))
                            print(f"\n{Fore.GREEN+total_accounts+Fore.RESET} Profil(s) trouvés")
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass

def user_actions():
    u = input("Username : ")
    print("\r")
    usrchk(usernamee=u)
    print("\r")
    input('Press [Enter] to continue :\n')
    user_actions()
user_actions()