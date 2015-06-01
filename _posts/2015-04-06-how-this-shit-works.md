---
layout: post
title: how this shit works.
date: {}
published: true
---


## so... basically this is it:
- make sure u have `node_modules` in your `.gitignore`
- set markdown syntax to `kramdown` in your `_config.yml`
- run `npm install` to grab all dependencies from your `package.json`
- run `gulp` to open up `localhost:3000` and start editing what u need
- if all is ok, just commit to the repo and sync.

### but...
if you have all repos saved locally and up-to-date (that is, working on one comp), then u don't need to install gulp locally every time. branches are easy since they work on the same files. tadaa.
