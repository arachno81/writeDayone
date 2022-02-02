import webbrowser, urllib.parse, datetime, subprocess, time

dt_now = datetime.datetime.now()
print(dt_now.strftime('%Y/%m/%d/%H:%M:%S'))
text = input('[make journal]\n=> ')
if text == 'x':
  print('oh')
else:
  time.sleep(0.3)
  print('...')
  time.sleep(0.3)
  print('..')
  time.sleep(0.3)
  print('.')
  text = urllib.parse.quote(text)
  url = "dayone://post?entry=" + text
  print(url)
  webbrowser.open(url)
  time.sleep(3)
  kil = "pkill -x Day\ One"
  subprocess.run(kil,shell=True)
  print('bye')
  