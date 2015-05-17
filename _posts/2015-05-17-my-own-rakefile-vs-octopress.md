---
layout: post
title:  "my own rakefile vs octopress?"
date:   2015-05-17 21:35:30
categories: jekyll update
---

i need to fix this. need a faster way to create posts.

rake new_show["title"]
rake new_event["title"]

or something like this...

got something but it doesn't seem to work...

```
[ master ] $ rake post --trace
** Invoke post (first_time)
** Execute post
rake aborted!
NoMethodError: undefined method `[]' for nil:NilClass
```

blaarg....