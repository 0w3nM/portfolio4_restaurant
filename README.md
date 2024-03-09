# Galaxy Gourmet Website 
The Galaxy Gourmet site offers users a chance book a table at a family friendly restaurant, where the whole family can relax and enjoy succulent meals.
The restaurant allows users to create an account so that they may see their own reservations to update or remove if needed.
It also offers a menu and times for booking along with socila media accounts to follow to stay upto date with the restaurant.
There are various fonts used to make the website feel less bland. They are Oswald,Playpen Sans, Skranji, Titillium Web 300 and also sans-serifs as a back up font.

# -Features-

  #### Favicon:

  - Favicon is dispalyed on the tab with the title of the page.

 ![Favicon](media/images/pp4_favicon_and_name.png)  

  #### Title:

  - The title is also a link that will bring the user back to see the menu.

 ![Title](media/images/pp4_title_unhighlighted.png)

 -  The top image shows the link, when the user hasnt hovered over it.

 ![Title](media/images/pp4_title_highlighted.png)

 - The bottom image shows the link when the user hovers over it and it changes colour.

 ### Welcome Message:
 - A welcome message is shown to the users that tells the users what information is.

 ![Message](media/images/pp4_welcome_message.png)

#### Menu Title:

 - A title showing users where the menu is.
  
 ![Menu Title](media/images/pp4_menu_title.png)  

 #### Menu:
  
  - The menu shows what types of foods and drinks are avaiable.

 ![Top Menu](media/images/pp4_top_menu.png)
 ![Bottom Menu](media/images/pp4_bottom_menu.png)

#### Time:
  
   - Times that are available to book are shown under the menu.
  
  ![Times](media/images/pp4_times.png)

#### Social Media:
  
  - The social media profiles are placed at the bottom of the page for users to click.
  
 ![Times](media/images/pp4_social_media_links.png)

 #### Creating a reservation:
  
  - Form to create a reservation.

  ![Reservation Form](media/images/pp4_reservation_form.png)

#### Reservations:

 - Reservations are all shown on this page to be view updated and deleted.
  
  ![Details](media/images/pp4_reservation_made.png)

#### User only Reservation:

  - The reservations are only show to the User that is logged in and made it.

  ![User Only Reservation](media/images/pp4_user_only_reservation.png)

#### Updating a reservation:
  
 - Form to update users reservation and success message. Images are placed at the bottom on the page to entice the user in placing an reservation to try the food.

  ![Update Form](media/images/pp4_reservation_updated.png)
  ![Success Message](media/images/pp4_update_confirmantion.png)
  

#### Deleting Reservations:

 - Reservations are removed once the delete button is pressed with a confirmation message.
  
  ![Delete](media/images/pp4_deleted_reservation.png)


#### Account Creation and sign in bar:
  
   - Allows new and existing users to make an account or sign in to one the already have.

  ![Account Nav Bar](media/images/pp4_signed_out_nav_bar.png)

#### Sign Out:

  - Users have the ablity to sign out of thier account, with a success message.
  
  ![Sign Out](media/images/pp4_signout_page.png)
  ![Success Message](media/images/pp4_sign_out_confirmation.png)

#### Sign In:
  
  - Page allows users to sign in with their details with a success message.

  ![Sign in Page](media/images/pp4_login.png)
  ![Success Message](media/images/pp4_sign_in_confirmation.png)

#### Sign Up page:

 - Page allows users to make an account.
  
  ![Sign up](media/images/pp4_account_register.png)


#### Images:
  - Below are the images that were used as the background images for the html pages.

  ![Burger](media/images/pp4_background_image_burger.jpg)

  - The Burger is used on the landing page that the users see.

  ![Steak](media/images/pp4_background_image_steak.jpg)

  - The Steak is used when the user is veiwing their reservations.

  ![Ice Cream](media/images/pp4_background_image_ice-cream.jpg)

  - The Ice Cream is on the page for when a user is creating an account.

  ![Pasta](media/images/pp4_background_image_pasta.jpg)

  - The Pasta is used for the page when the user is creating a reservation.

  ![Pizza](media/images/pp4_background_image_pizza.jpg)

  - The pizza is used when the user signs in.

  ![Soup](media/images/pp4_background_image_soup.jpg)

  - The Soup is used on the logout page.
    

# -Technologies used-

- HTML
- CSS
- Bootstrap
- JavaScript
- Python
- Postgresql  
- Cloudinary
- Django allauth library
- Django
- Gunicorn
- Elephantsql
- Google fonts

# -Testing-
-Testing can be found on this page:[TESTING.md](TESTING.md)



# -Deployment-
    Deploying on Heroku:

- Create an account on Heroku.
- Click on a new app.
- In the settings, got to the Config Vars.
- In the Config Vars, add the Enviroment Variables.
- Go to the Deploy tab and select Github to connect to.
- Search for the Repository required and select once found.
- Choose between Automatic or Manual Deploy.
- Once built got to Open App at the top of the page.
- Page will be deployed if successfully built.

## -Web Browser used -

  - Chrome

## -Devices Used -

  - 12th Gen Intel (R) Core TM i7-12700F - Desktop

# -Credits-

## Content

  - 'I think before i blog' walkthrough was used as a template to help create the project through [CodeInstitute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/). 
  - Other students questions and previous projects on the the same subject such as [Garth McGirr](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak/blob/main/README.md) & [Ali Okeeffe](https://github.com/AliOKeeffe/PP4_My_Meal_Planner/blob/main/README.md) were used as a guide and further understand on the project creation through [Slack](https://slack.com/intl/en-gb/get-started#/createnew).  
  - An image was placed on the browser tab and was created through [Favicon](https://www.favicon.cc/).
  - To show messages to the user, this website offered helpful tips on how to show the [Messages](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/#using-messages-in-views-and-templates/).
  - When i came across an error, i found help when i used a link from [Positonal Arguments](https://stackoverflow.com/questions/68572656/django-missing-1-required-positional-argument-id/).
  - When i struggled and needed to understand the fix i looked at page for [Views](https://stackoverflow.com/questions/26258905/the-view-didnt-return-an-httpresponse-object-it-returned-none-instead/) i also used this link for help on [Views](https://docs.djangoproject.com/en/4.2/ref/class-based-views/base/#django.views.generic.base.View/).
  - When it came to view forms as a paragraph and understand the process better i used the link on [Paragraph](https://www.geeksforgeeks.org/form-as_p-render-django-forms-as-paragraph/).
  - I got a error message and to solve the issue i used the link for [NoReverseMatchError](https://stackoverflow.com/questions/38390177/what-is-a-noreversematch-error-and-how-do-i-fix-it/).
  - When i was stuck on the understanding on the usage of was used i looked into [allauth](https://docs.allauth.org/en/latest/).
  - Understanding the styling  of my project was used with [Grid](https://materializecss.com/grid.html/) and when the colors were needed, i used both a bootstrap site for their tips on [Colors](https://getbootstrap.com/docs/5.0/utilities/colors/) &  i also used this site for their helpful tips on [Color](https://materializecss.com/color.html/).
  - When it came to creating a form for my project i used 2 different links. The first was this link on how to craft a [Form](https://docs.djangoproject.com/en/4.2/topics/forms/), and the second was a video on [YouTube](https://www.youtube.com/watch?v=ncradqkSzCw/).
  - Trying to add a function to stop users selecting previous dates i reached out for help from [Tutors](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentpredictiveanalytics/tutor). I also used links to gain understanding on the issue, the first being from [Avoidence of past date booking](https://stackoverflow.com/questions/70671189/avoid-booking-past-dates-with-django), the second on creating a [Date picker](https://stackoverflow.com/questions/74227268/how-to-make-a-date-picker-that-does-not-select-previous-dates-in-django) and finally how to prevent the DateField picking [Previous dates](https://stackoverflow.com/questions/15751976/how-to-prevent-datefield-record-addition-for-past-days-in-django).
  - I came across a problem that had a dropdown menu, showing all the Users, i wanted to hide this being shown so i asked for help from a [Tutor](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentpredictiveanalytics/tutor) which they pointed me towards the blog [Walkthrough](https://github.com/Code-Institute-Solutions/blog/blob/main/14_where_to_put_things/03_tidy_up/blog/views.py).
  - I needed to place defensive coding to stop Users from accessing the site through URL, i used a link through [Stackoverflow](https://stackoverflow.com/questions/47244036/using-django-login-required-mixin), aswell as this link from [Stackoverflow](https://stackoverflow.com/questions/56567529/allowing-url-access-only-to-logged-in-users), i also used help from Tutors on [CodeInstitue](https://learn.codeinstitute.net/ci_support/diplomainfullstacksoftwarecommoncurriculum/tutor).
  - I came across an issue that showed all the reservations made by users on the same page, so i looked for help through [Stackoverflow](https://stackoverflow.com/questions/71224300/how-to-show-only-the-data-of-the-user-that-is-logged-in-django), i also asked for help from Tutors through [CodeInstitue](https://learn.codeinstitute.net/ci_support/diplomainfullstacksoftwarecommoncurriculum/tutor).

## -Media-

  - Images for the background of the pages were taken and used from [Pexels](https://www.pexels.com/)