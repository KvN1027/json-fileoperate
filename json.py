import json
###
# 讀
###
with open(r"static/data.json") as f:
  p = {}
  p = json.load(f)
  f.close()
###
# 寫
###
with open(r"static/data.json",'w') as f:
  json.dump(p,f)
  f.close()
  return redirect('/'+request.values['name'])
