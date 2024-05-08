def args(**kwarg):
    return {v:k for k,v in kwarg.items()}# it is same like list comphersion but it is a dictonary comphersiomn and syntax
#dict{key:value for item in itrablr  for item in iterable }
print(args(a=1, b=2, e=3))
print(args(a=1, b=2))