---
layout: post
title:  "my own rake tasks"
date:   2015-05-17 21:35:30
categories: jekyll update
---

seems i got it too work. i needed a faster way to create posts with a simple command on the command line: `rake post["title"]`

in a `_post.txt` file i can define the yaml front matter for the specific post and the rakefile takes care of the title and date of the post and generates the file inside `_posts/`.

in the `_config.yml` i add the lines:

    post:
      template: _post.txt
      extension: md


i can add different tasks for different post types which could have different front matter if needed. booya.