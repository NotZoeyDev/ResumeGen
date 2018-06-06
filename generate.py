import json, os, sys, shutil, codecs

toVerifiy = ["config.json", "src/", "src/imgs/", "src/section.html", "src/style.css", "src/template.html"]

print("Verifying everything is good...\n")

# Making sure that every file needed is here
for v in toVerifiy:
	if os.path.exists(v):
		print("File " + v + " found!")
	else:
		print("File " + v + " is missing!")
		print("Please refer to https://github.com/NotZoeyDev/ResumeGen for more information.")
		sys.exit(1)

# Removing an old build directory if there's one.
if os.path.exists("build/"):
	print("\nRemoving the last build.")
	shutil.rmtree("build/")

print("Creating temporary folder...")

try:
	os.mkdir("build")
	print("Created successfully!")
except:
	print("Couldn't create temporary folder!")
	print("Check the folder permission...")
	sys.exit(1)

print("\nGenerating your resume page...\n")

json_file = open("config.json", "r")
parsed_json = json.loads(json_file.read())
json_file.close()

template_html = open("src/template.html", "r").read()

# Basically generate the whole HTML file.
try:
	print("\tRenaming some lines...")
	template_html = template_html.replace("{title}", parsed_json["title"])
	template_html = template_html.replace("{name}", parsed_json["name"])
	print("\tAdding color")
	template_html = template_html.replace("{header-color}", parsed_json["color"])
	template_html = template_html.replace("{theme-color}", parsed_json["color"])
	print("\tAdding the favicon")
	template_html = template_html.replace("{favicon}", parsed_json["icon"])
	shutil.copy2("src/" + parsed_json["icon"], "build/")

	section_container = ""
	sections = 0

	print("\tCreating the sections:\n")
	for p in parsed_json["projects"]:
		print("\t\tGenerating the " + p + " section!")
		section_file = open("src/section.html", "r")
		section_template = section_file.read()
		section_file.close()

		print("\t\tSetting the section name.")
		section_template = section_template.replace("{section-name}", p)

		print("\t\tAdding some color to it.")
		project_data = parsed_json["projects"][p]
		section_template = section_template.replace("{section-background-color}", project_data["color"])

		if sections % 2 == 1:
			section_template = section_template.replace("{class}", 'class="reversed"')
		else:
			section_template = section_template.replace("{class}", '')

		print("\t\tGenerating some text and links.")
		section_about = ""
		for a in project_data["about"]:
			section_about += "<p>" + a + "</p>\n\t\t\t\t\t"

		for l in project_data["links"]:
			section_about = section_about.replace("<" + l + ">", '<a href="' + project_data["links"][l] + '">' + l + "</a>")

		print("\t\tAdding the text and links.")
		section_template = section_template.replace("{section-text}", section_about)

		print("\t\tSetting the picture...")

		if os.path.exists("src/imgs/" + project_data["filename"]):
			print("\t\tThe " + project_data["filename"] + "file was found, setting it.")
		else:
			print("\t\tThe file " + project_data["filename"] + " wasn't found!")
			print("\t\tThis won't cause any errors, but you should fix it manually.")

		section_template = section_template.replace("{section-image-name}", project_data["filename"])

		print("\t\tThe section " + p + " was generated succesfully!\n")
		section_container += section_template + "\n"

		sections += 1

	print("\tAdding the sections to the template!")
	template_html = template_html.replace("{section-container}", section_container)

	print("\tEditing the \"about me\" section.\n")
	about_info = parsed_json["about"]

	print("\t\tAdding a title.")
	template_html = template_html.replace("{about-me-title}", about_info["title"])

	print("\t\tAdding some text.")
	about_text = ""
	for t in about_info["text"]:
		about_text += "<p>" + t + "</p>\n\t\t\t\t\t"

	print("\t\tSetting the background color")
	template_html = template_html.replace("{about-color}", about_info["color"])

	print("\t\tAdding the contact links.")
	contact_links = ""
	for c in about_info["contact"]:
		contact_links += "<p><a href=\"" + about_info["contact"][c]["link"] + "\">" + about_info["contact"][c]["account"] + "</a> (" + c + ")</p>\n\t\t\t\t\t"

	print("\t\tAdding the text and links to the template.\n")
	template_html = template_html.replace("{about-me-text}", about_text) 
	template_html = template_html.replace("{contact-links}", contact_links)

except:
	print("Something went horribly wrong!")
	print("Make sure that your config.json is correct.")
	sys.exit(1)

print("\tHTML Generation is done!\n")
print("Exporting everything to the build folder.")

try:
	index_html = codecs.open("build/index.html", "w+", encoding="utf-8")
	index_html.write(template_html)
except:
	print("An error happened when writing the index.html file!")
	print("Check if you have the correct permissions.")
	sys.exit(1)

print("index.html generated...")
print("copying style.css")

try:
	shutil.copy2("src/style.css", "build/")
except:
	print("An error happened when copying the style.css file!")
	print("Check if you have the correct permissions.")
	sys.exit(1)


print("style.css copied!")
print("Copying images...")

try:
	os.mkdir("build/imgs")

	for img in os.listdir("src/imgs/"):
		shutil.copy2("src/imgs/" + img, "build/imgs/")
except:
	print("An error happened when copying images!")
	print("Check if you have the correct permissions.")
	sys.exit(1)

print("Images copied!\n")

print("Your new resume has been exported at " + os.getcwd() + "/build/\n")
print("Simply copy its content to your web server and it should work without any problem.")
print("Thank you for using ResumeGen!")
print("By @NotZoeyDev")