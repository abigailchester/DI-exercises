name = input("Enter your full name here")

phone = input("type your phone number here")

address = input("type your email address")

email = input("type your email address here")

linkedin = input("type in your linkedin url here")

github = input("type your github profile here")

jobtitle1 = input("type in your most recent job title")

jobcompany1 = input("which company?")

jobdate1 = input("when did you work there?")

joblocation1 = input("what location/city?")

descriptionBP1 = input("add bulletpoint description here")

descriptionBP2 = input("insert another description bulletpoint")

descriptionBP3 = input("add one more description bulletpoint")

jobtitle2 = input("what is your next most recent job title?")

jobcompany2 = input("which company?")

jobdate2 = input("when did you work there?")

joblocation2 = input("what location/city?")

description2BP1 = input("add bulletpoint description here")

description2BP2 = input("insert another description bulletpoint")

description2BP3 = input("add one more description bulletpoint")

degree1 = input("what is your most recent degree in school? what did you study?")

school1 = input("what school was it from?")

schooltime1 = input("when did you study there?")

schoolplace1 = input("where was the school located?")

degree2 = input("what is your next most recent degree of education?")

school2 = input("what school was it from?")

schooltime2 = input("when did you study there?")

schoolplace2 = input("where was the school located?")

skill1 = input("add a skill")

skill2 = input("add another skill")

skill3 = input("add another skill")

skill4 = input("add one more skill")

extra1 = input("add an extracurricular activity")

extra2 = input("add another extracurricular activity")

extra3 = input("add another extracurricular activity")

extra4 = input("add one more extracurricular activity")


html = f'''
<!DOCTYPE html>
<html>
<head>
	<title>Your Generated CV</title>

</head>
<body>

<h1 class="name">{name}</h1>

<div class="contact">
	<div id="phone">Phone: {phone}</div>
	<div id="email">Email: {email}</div>
	<div id="address">Address: {address}</div>
	<div id="linkedin">Linkedin: {linkedin}</div>
	<div id="github">Github: {github}</div>
</div>

<div class="main">
	<div id="column1">
		<div class="experience">
			<h2><u>Work Experience</u></h2>
			<div class="jobDescription">
				<h3>{jobtitle1}</h3>
				<h4>{jobcompany1}</h4>
				<h5>{jobdate1}</h5>
				<h5>{joblocation1}</h5>
				<ul>
					<li>{descriptionBP1}</li>
					<li>{descriptionBP2}</li>
					<li>{descriptionBP3}</li>
				</ul>
			</div>
			<div class="jobDescription">
				<h3>{jobtitle2}</h3>
				<h4>{jobcompany2}</h4>
				<h5>{jobdate2}</h5>
				<h5>{joblocation2}</h5>
				<ul>
					<li>{descriptionBP1}</li>
					<li>{descriptionBP2}</li>
					<li>{descriptionBP3}</li>
				</ul>				
			</div>
		</div>
	</div>
	<div id="column2">
		<div class="education">
			<h2><u>Education</u></h2>
			<div class="schoolDescription">
				<h3>{degree1}</h3>
				<h4>{school1}</h4>
				<h5>{schooltime1}</h5>
				<h5>{schoolplace1}</h5>
			</div>
			<div class="schoolDescription">
				<h3>{degree1}</h3>
				<h4>{school2}</h4>
				<h5>{schooltime1}</h5>
				<h5>{schoolplace2}</h5>
			</div>
		</div>

		<div class="skills">
			<h2><u>Skills</u></h2>
			<ul>
				<li>{skill1}</li>
				<li>{skill2}</li>
				<li>{skill3}</li>
				<li>{skill4}</li>
			</ul>
		</div>

		<div class="extracurricular activities">
			<h2><u>Extracurricular Activities</u></h2>
			<ul>
				<li>{extra1}</li>
				<li>{extra2}</li>
				<li>{extra3}</li>
				<li>{extra4}</li>
			</ul>
		</div>
	</div>
</div>
</body>
</html>'''
print(html)
file = open("cv.html","w")
file.write(html) 
file.close() 



