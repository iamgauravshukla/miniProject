print(" **********     Welcome to Website Builder     **********")
print("Website you want \n 1 : Resume \n 2 : Tech Company ")
select = int(input("Choose 1 or 2 \n"))


# Resume Starts
def resume():
    print("\nGuidelines : Please Follow all the steps carefully. \n"
          "Step 1 : Add your photo in img folder.\n"
          "Step 2 : Enter all details carefully as per instructions.\n")
    skills = []
    lang_li = []

    # Basic Details
    name = input("Enter your full name : ")
    work_profile = input("Enter your work profile. eg: (Web Developer) : ")
    profilePhoto = input("Enter profile image file name with extension eg (gaurav.jpg) : ")
    about = input("Enter about you in brief (50-80 words) : \n")

    # Skills
    print("Enter Your Top 4 Skills : ")
    for i in range(0, 4):
        skill = input(f"Skill-{i + 1} : ")
        skills.append(skill)

    # Education
    print("Enter Your Education Details : ")

    current_Degree = input("Current/Recent Degree : ")
    current_College = input("College name : ")
    current_year = input("Start year and Completion year eg(2017-2021) :  ")

    sr_secStream = input("XII - Stream : ")
    sr_secCollege = input("College name : ")
    sr_secYear = input("Start year and Completion year : ")

    x_college = input("High Scholl (X) School Name : ")
    x_year = input("Start and End Year : ")

    # Speaking Languages
    print("Enter speaking languages you know : ")
    for i in range(0, 3):
        language = input(f"Language {i + 1} : ")
        lang_li.append(language)

    # Contact Details
    address = input("Enter your address : ")
    mobile = input("Enter your mobile number : ")
    email = input("Enter your email : ")
    website = input("Enter your website url : ")

    # Work Experience
    print("Enter your recent work Experience : ")
    post = input("Designation of your work eg(Web Developer/Data Analyst) :  ")
    company = input("Enter Company/Organization name : ")
    workYear = input("Start and Current/End Year : ")
    workDis = input("Describe your work role in few words :\n")

    file = open("resume.html", 'w')
    file.write("<!DOCTYPE html>\n"
               '<html lang="en">\n'
               "<head>\n"
               '    <meta charset="UTF-8">\n'
               '    <meta name="viewport" content="width= device-width">\n'
               '    <script src="https://kit.fontawesome.com/64a6227cb0.js" crossorigin="anonymous"></script>\n'
               '    <link href="https://fonts.googleapis.com/css2?family=Merienda:wght@700&display=swap" rel="stylesheet">\n'
               '    <link href="https://fonts.googleapis.com/css2?family=Sanchez&display=swap" rel="stylesheet">\n'
               '    <link rel="stylesheet" href="css1/style.css">\n'
               '    <link rel="stylesheet" href="css1/responsive.css">\n'
               f"   <title> {name}-{work_profile}</title>\n"
               "</head>\n"
               "\n"
               "<body>\n"
               '    <div id="head">\n'
               '        <div class="details">\n'
               f'           <img src="img/{profilePhoto}">\n'
               f'           <h2 class="name" > Hi, I am {name} </h2>\n'
               f'           <h2 class="job"> {work_profile} </h2>\n'
               "        </div>\n"
               "    </div>\n"
               "\n"
               '<div id="container">\n'
               '    <div class="about">\n'
               '        <div class="about-left">\n'
               '            <h2 class="h-primary2"> About Me </h2>\n'
               f"           <p> {about} </p>\n"
               "        </div>\n"
               '        <div class="about-right">\n'
               '            <h2 class="h-main">Skills</h2>\n'
               f"           <p>{skills[0]}</p>\n"
               '            <div class="skill-1 skill"><p>90%</p></div>\n'
               f"           <p>{skills[1]}</p>\n"
               '            <div class="skill-2 skill"><p>70%</p></div>\n'
               f"           <p>{skills[2]}</p>\n"
               '            <div class="skill-3 skill"><p>80%</p></div>\n'
               f"           <p>{skills[3]}</p>\n"
               '            <div class="skill-4 skill"><p>90%</p></div>\n'
               "        </div>\n"
               "    </div>\n"
               '    <div class="education">\n'
               '        <div class="edu-left">\n'
               '            <h2 class="h-main">Education</h2>\n'
               f'           <h3 class="course">~ {current_Degree}</h3>\n'
               f'           <p class="college">{current_College} &nbsp; &nbsp; {current_year}</p>\n'
               f'            <h3 class="course">~ XII from {sr_secStream}</h3>\n'
               f'            <p class="college">{sr_secCollege} &nbsp; &nbsp; {sr_secYear}</p>\n'
               '            <h3 class="course">~ X</h3>\n'
               f'            <p class="college">{x_college} &nbsp; &nbsp; {x_year}</p>\n'
               "       </div>\n"

               '        <div class="edu-right">\n'
               '               <h2 class="h-primary2">Languages</h2>\n'
               f"                <ul>\n<li>{lang_li[0]}</li>\n<li>{lang_li[1]}</li>\n<li>{lang_li[2]}</li>\n</ul>"
               "        </div>\n"
               "    </div>\n"

               '    <div id="contact">\n'
               '        <div class="contact-left">\n'
               "            <h2>Contact</h2>\n"
               f'            <p><i class="fas fa-map-marker-alt"></i>&nbsp; {address}</p>\n'
               f'            <p><i class="fas fa-mobile-alt"></i>&nbsp; +91 {mobile}</p>\n'
               f'            <p><i class="fas fa-envelope-open-text"></i>&nbsp; {email}</p>\n'
               f'            <p><i class="fas fa-globe"></i>&nbsp; {website}</p>\n'
               "        </div>\n"
               '        <div class="contact-right">\n'
               '            <h2 class="h-main">Experience</h2>\n'
               f'            <h3 class="course">{post}</h3>\n'
               f'            <p class="para">{company} &nbsp; &nbsp; {workYear}</p>\n'
               f'            <p class="para">{workDis}</p>\n'
               "        </div>\n"
               "    </div>\n"

               '    <div class="footer">\n'
               '        <p class="para">Copyright &copy; 2020 | Developed and designed by Gaurav Shukla</p>\n'
               "    </div>\n"

               '    <div class="social-icons">\n'
               '        <div class="icon">\n'
               '            <i class="fab fa-instagram"></i>\n'
               "        </div>\n"

               '        <div class="icon">\n'
               '            <i class="fab fa-linkedin"></i>\n'
               "        </div>\n"

               '        <div class="icon">\n'
               '            <i class="fab fa-github"></i>\n'
               "        </div>\n"

               '        <div class="icon">\n'
               '            <i class="fab fa-google-plus-g"></i>\n'
               "        </div>\n"
               "    </div>\n"
               "</div>\n"
               "</body>\n"
               "</html>"
               )
    file.close()



# Resume Ends Here

# Company Website Starts Here
def company():
    print("\nGuidelines : Please Follow all the steps carefully. \n"
          "Step 1 : Add your photo in img folder.\n"
          "Step 2 : Enter all details carefully as per instructions.\n")
    com_name = input("Enter your company name here : ")
    tagline = input("Enter your company tagline (if have any) : ")
    logo = input("Branding name or logo name : ")
    welcome = input("Write welcome line or brief intro of company : ")
    aboutUs = input("Write about us of your company (in 50-100 words) : ")
    print("Enter about services your company provide : ")
    service_Li = []

    for i in range(0, 3):
        service = input(f"Service {i + 1}: ")
        serviceDis = input(f"Describe in brief about service{i + 1} : ")
        service_Li.append(service)
        service_Li.append(serviceDis)

    file = open("company.html", 'w')
    file.write(
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width">\n'
        '<link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Itim&display=swap" rel="stylesheet">\n'
        '<link rel="stylesheet" type="text/css" href="css2/style.css">\n'
        '<link rel="stylesheet" type="text/css" media ="screen and (max-width : 1125px)" href="css2/phone.css">\n'
        '<link rel="stylesheet" type="text/css" media ="screen and (max-width : 540px)" href="css2/xsphone.css">\n'
        f'<title>{com_name} - {tagline}</title>\n'
        '</head>\n'
        '<body>\n'

        '<nav id="navbar">\n'
        '<div class="logo">\n'
        f'<h2>{logo}</h2>\n'
        '</div>\n'
        '<ul>\n'
        '<li class="item">\n'
        '<a href="#">Home</a>\n'
        '</li>\n'
        '<li class="item">\n'
        '<a href="#about">About Us</a>\n'
        '</li>\n'
        '<li class="item">\n'
        '<a href="#1">Services</a>\n'
        '</li>\n'
        '<li class="item">\n'
        '<a href="#contact">Contact us</a>\n'
        '</li>\n'
        '</ul>\n'
        '</nav>\n'

        '<section id="home">\n'
        f'<h1 class="h-primary center">Welcome to {com_name}</h1>\n'
        f'<p>{welcome}</p>\n'
        '<a href="#1"><button class="btn">Know More</button></a>\n'
        '</section>\n'

        '<section id="about">\n'
        '<h1 class="h-primary center">About Us</h1>\n'
        '<div class="about-main">\n'
        '<div class ="about-img">\n'
        '<img src="img/about.jpg">\n'
        '</div>\n'
        '<div class="about-content">\n'
        f'<p>{aboutUs}</p>\n'
        '</div>\n'

        '</div>\n'
        '</section>\n'

        '<section class="service-container" id="1">\n'
        '<h1 class="h-primary center">Our Services</h1>\n'
        '<div id="services">\n'
        '<div class="box">\n'
        '<img src="img/1.png" class="img">\n'
        f'<h2 class="h-secondary">{service_Li[0]}</h2>\n'
        f'<p>{service_Li[1]}</p>\n'
        '</div>\n'
        '<div class="box">\n'
        '<img src="img/2.png" class="img">\n'
        f'<h2 class="h-secondary">{service_Li[2]}</h2>\n'
        f'<p>{service_Li[3]}</p>\n'
        '</div>\n'
        '<div class="box">\n'
        '<img src="img/3.png" class="img">\n'
        f'<h2 class="h-secondary">{service_Li[4]}</h2>\n'
        f'<p>{service_Li[5]}</p>\n'
        '</div>\n'
        '</div>\n'
        '</section>\n'

        '<section id="client-section">\n'
        '<h1>Our Clients</h1>\n'
        '<div id="clients">\n'
        '<div class="client-item">\n'
        '<img src="img/logo1.png" alt="Our Client">\n'
        '</div>\n'
        '<div class="client-item">\n'
        '<img src="img/logo2.png" alt="Our Client">\n'
        '</div>\n'
        '<div class="client-item">\n'
        '<img src="img/logo3.png" alt="Our Client">\n'
        '</div>\n'
        '<div class="client-item">\n'
        '<img src="img/logo4.png" alt="Our Client">\n'
        '</div>\n'
        '</div>\n'
        '</section>\n'

        '<section id="contact">\n'
        '<h1 class="h-primary center">Contact Us</h1>\n'
        '<div id="contact-form">\n'
        '<form action="">\n'

        '<div class="userInput">\n'
        '<input type="text" name="name" placeholder="Enter Your Name ">\n'
        '</div>\n'

        '<div class="userInput">\n'
        '<input type="text" name="email" placeholder="Enter Your Email ">\n'
        '</div>\n'

        '<div class="userInput">\n'
        '<input type="phone" name="mobile" placeholder="+91 1234567890">\n'
        '</div>\n'

        '<div class="userInput">\n'
        '<input type="text" name="subject" placeholder="Subject">\n'
        '</div>\n'

        '<div class="userInput">\n'
        '<textarea placeholder="Message"></textarea>\n'
        '</div>\n'

        '<div class="userSubmit">\n'
        '<input type="submit" value="submit">\n'
        '</div>\n'
        '</form>\n'
        '</div>\n'
        '</section>\n'
        '<footer class="center"> Copyright&copy; 2020 | Designed by Gaurav | All rights reserved </footer>\n'
        '</body>\n'
        '</html>'
    )
    file.close()


# Company Website Ends Here

if select == 1:
    resume()
elif select == 2:
    company()
else:
    print("Invalid Option")

print("******* Thank You *******")
