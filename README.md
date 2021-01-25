# treelinefmt

Generate and edit formats within TreeLine outliner documents.

# Status

**JUST STARTING** -- 2021-01-23

# What Treeline Is and What This Is For

[TreeLine is a fascinating cross between an outliner and a database.](https://treeline.bellz.org/index.html)

Some of it's great features include:
* Structured data can be attached to any node.
* The same node can appear multiple times within the tree.
* All data is recorded in and parsed from JSON.

I use it for more and more of my electronic notekeeping.

However, one difficulty I have with it, is in maintaining the formats.  Remember that piece about "structured data can be attached to any node?"  Well, how that works is that a node is assigned a user-defined "format."  There are tools within the TreeLine program that help you to design and maintain a given format, but I found that as my system got more complex, that the built-in tool was less and less what I needed for maintaining my complex library of formats.  So I started this project, to help me create and manage formats in TreeLine.

# Ambitions

I anticipate (today is 2021-01-23) that my development of this program will go through the following stages:
1. First, I'll be setting up a basic code infrastructure, and the tool and format will be specifically structured around the formats that I rely on.  There will be a lot of hard-coding, and it might not be so useful to others.
2. As time passes and my needs generalize, I suspect that the tool will generalize as well.  Then, this might be more useful to people other than myself.
3. If I continue to work on this project, I anticipate having a whole system for importing and exporting formats, and maintaining consistencies between formats.  If it reaches this point, then it should be maximally useful to others working with TreeLine.

Perhaps some of the ideas from this code will make it into TreeLine proper at some point.  I don't know.

