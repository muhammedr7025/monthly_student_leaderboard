from PIL import Image, ImageDraw, ImageFont
from numerize import numerize
from io import BytesIO
import requests
background = Image.open("Dboard.png")
karma_color = "rgb(255, 80, 89)"
color = "white"
font = ImageFont.truetype("PlusJakartaSans-Bold.ttf", 33) # size of name
font_karma = ImageFont.truetype("Inter-Black.ttf", 26)  #size of karma
font_karma1 = ImageFont.truetype("Inter-Black.ttf", 20)  #size of karma
total_score = {'434916213064466844': {'full_name': 'Akash R Chandran', 'karma': 12544, 'orgs': [ 'St Thomas Institute of Science and Technology']},'434916213064466474': {'full_name': 'Angel Rose A G', 'karma': 12544, 'orgs': [ 'St Thomas Institute of Science and Technology']}, '739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739001298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739038298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']}, '821366753594310476': {'full_name': 'dhannu d', 'karma': 600, 'orgs': [None]},'434916213064466444': {'full_name': 'Muhammed R', 'karma': 12544, 'orgs': [ 'St Thomas Institute of Science and Technology']},'434916213064466474': {'full_name': 'Muhammed R', 'karma': 12544, 'orgs': [ 'St Thomas Institute of Science and Technology']}, '739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365217': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739001298450365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'439038298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']}, '121366753594310476': {'full_name': 'dhannu d', 'karma': 600, 'orgs': [None]},'434916213064466444': {'full_name': 'Muhammed R', 'karma': 12544, 'orgs': [ 'St Thomas Institute of Science and Technology']},'434916213064466474': {'full_name': 'Muhammed R', 'karma': 12544, 'orgs': [ 'St Thomas Institute of Science and Technology']}, '739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739001298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739038298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']}, '821366753594310476': {'full_name': 'dhannu d', 'karma': 600, 'orgs': [None]},'434916213064466444': {'full_name': 'Muhammed R', 'karma': 12544, 'orgs': [ 'St Thomas Institute of Science and Technology']},'434916213064466474': {'full_name': 'Muhammed R', 'karma': 12544, 'orgs': [ 'St Thomas Institute of Science and Technology']}, '739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739068298430365217': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739001298450365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'439038898430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']}, '121366763594310476': {'full_name': 'dhannu d', 'karma': 600, 'orgs': [None]}}
font_college = ImageFont.truetype("PlusJakartaSans-Bold.ttf", 18) #size of college
x, y = 95,290
c = 1
j=0
for discord_id, data in total_score.items():
    if c > 13:
        break

    url = "https://assets.mulearn.org/misc/user.png"
    avatar = BytesIO(requests.get(url).content)
    im = Image.open(avatar)
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.LANCZOS)
    im.putalpha(mask)
    im = im.resize((115, 115)) #size of image
    draw = ImageDraw.Draw(background)
    background.paste(im, (x+25, y+40), im)

    name = "Vinu Balagopal"
    if len(name) > 18:
        name = name.split(" ")
        if len(name) > 1:
            name = name[0] + " " + name[1]
            if len(name) > 19:
                name = name.split(" ")
                name = name[0] + " " + name[1][0].capitalize()
        else:
            name = str(name[0])
    draw.multiline_text((x+155,y+80), name, fill="rgb(7, 46, 101)", font=font, align="center")
    name = "College of figma engineering"
    name = name.upper()
    if len(name) > 17:
        first_line = name[:25]
        second_line = name[25:].strip()
        if second_line and second_line[0].isalpha() and first_line[-1].isalpha():
            split_index = first_line.rfind(' ')
            if split_index == -1:
                split_index = 25
            second_line = name[split_index:].strip()
            first_line = name[:split_index].strip()
        draw.multiline_text((x + 155, y + 130), first_line + "\n" + second_line, fill="rgb(7, 46, 101)", font=font_college,
                            align="left")
    else:
        draw.multiline_text((x + 155, y + 130), name, fill="rgb(7, 46, 101)", font=font_college, align="center")

    r = numerize.numerize(13500)
    draw.multiline_text(
        (x + 200, y+42),
        r,
        fill=color,
        font=font_karma1,
        align="left",
    )
    rnew = numerize.numerize(1700)
    rnew = rnew+" ϰ"
    draw.multiline_text(
        (x+47, y+165),
        rnew,
        fill="rgb(7, 46, 101)",
        font=font_karma,
        align="left",
    )
    c = c + 1
    x = x + 600
    j = j + 1
    if j % 3 == 0:
        x=100
        j = 0
        y = y + 277
    # c = c + 1
    # y = y + 737
    # j = j + 1
    # if j % 3 == 0:
    #     i = i + 1
    #     j = 0
    #     y = 66
    #     x = x + 265
out = BytesIO()
background.save(out, format="PNG")
background.show()
out.seek(0)