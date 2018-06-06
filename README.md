# ResumeGen
A simple python script to generate a great looking resume/portfiolo static web page.

### Requirements
* Python

### How to use  
1. `git clone https://github.com/NotZoeyDev/ResumeGen`
2. `cd ResumeGen/`
3. `python generate.py`

### How to set it up
Using ResumeGen is pretty straight forward, either:
* Use the default `config.json` file and learn by yourself.
* Read the instructions down below.

# Editing config.json
Editing the config.json is pretty easy, take a look at the clean `config.json` and read down the instructions below, it should be prety easy to follow.

### Clean config.json
```js
{
	"title": "page-title",
	"name": "your-name",
	"color": "",
	"icon": "",

	"projects": {
		"project-name": {
			"about": [
				"Line 1",
				"Line 2",
				"Line 3 with a <link>"
			],
			"links": {
				"link": "link-goes-here"
			},
			"color": "#FFFFFF",
			"filename": "file.png"
		}
	},

	"about": {
		"title": "Who am I",
		"color": "#FFFFFF",
		"text" : [
			"A cool dev",
			"I make stuff",
			"Open-source is great"
		],

		"contact": {
			"Twitter": {
				"account": "name-goes-here",
				"link": "url-goes-here"
			}
		}
	}
}
```

### Title, name
The `title` and `name` tag doesn't do that much.
* `title` website title, shown in the title bar of your browser.
* `name` name shown in the front-page, shown in a "Hi, I'm `name`" format.
* `color` is the background color of the header, also used as the theme-color for browsers.
* `icon` will be the favicon used in browers

### Projects
The `projects` tag is the most complex tag of them all.  
It's where you set up your "projects", and it goes like this.

```js
"name-goes-here": {
	"about": [
		"Line 1",
		"Line 2",
		"Line 3, with a <link>"
	],
	"links": {
		"link": "url-goes-here"
	},
	"color": "#ffffff",
	"filename": "picture.jpg"
}
```

And now, explaination:
* `name-goes-here` is the name of the project, shown as a title.
* `about` is the project description, shown in multiple lines.
* `links` are the links used inside the about tag.
* `color` is any `#ffffff` formated color.
* `filename` is the name of the file showing up beside the text.

### Note

For links, all you gotta do is put your word between two `<>` like this `<link>`.  
Then simply "declare" your link inside the `links` item as shown up top.

#### For multiple projects

Simply add a comma at the end of the project like this `},` and then just copy-paste the default project JSON object.
It should look like this 
```js
	...
	"filename:": "picture.jpg"
}, 
"project-number-two": {
	"about": [
	...
```

### About
The `about` tag is pretty easy to understand, you have only a few things to set up:
* `title` is the title of the section, have something descriptive and good looking.
* `color` is the background color of the div containing the information.
* `text` is exactly like the `projects` about part, except it doesn't have link support.
* `contact` is all your contact information, see below for more information.

### Contact
```js
"service-name": {
	"account": "your-account-name",
	"link": "direct-link-to-account"
}
```

I don't think this one requires an explaination, just take note this show up in this format: `account-name (service-name)` on the page.

#### Last note
If you feel like my instructions are unclear, feel free to push a better version of it, English isn't my main tongue and my wording may be bad.  
I hope you all enjoy using this little tool I made purely for fun.  
