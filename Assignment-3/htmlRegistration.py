#!/usr/local/bin/python3
import cgitb 
cgitb.enable()
import cgi
import MySQLdb
import MySQLdb.cursors;

from wsgiref.simple_server import make_server

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='student',
    passwd='student',
    db='assignment3',
    cursorclass=MySQLdb.cursors.DictCursor
) 

cursor = db.cursor()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title> Registration Form  </title>
    </head>
    <body>
        <form action="" method="POST">
            <label for="title">Title - </label>
            <select name="title" id="title">
                <option value=""></option>
                <option value="Mr.">Mr.</option>
                <option value="Mrs.">Mrs.</option>
                <option value="Ms.">Ms.</option>
                <option value="Dr.">Dr.</option>
            </select></br>

            <label for="firstName">First Name - </label>
            <input type="text" name="firstName" value="" /><br/>

            <label for="lastName">Last Name - </label>
            <input type="text" name="lastName" value="" /><br/>

            <label for="street">Street - </label>
            <input type="text" name="street" value="" /><br/>

            <label for="city">City - </label>
            <input type="text" name="city" value="" /><br/>

            <label for="province">Province - </label>
            <input type="text" name="province" value="" /><br/>

            <label for="postalCode">Postal Code - </label>
            <input type="text" name="postalCode" value="" /><br/>

            <label for="country">Country - </label>
            <select name="country" id="country">
                <option value=""></option>
                <option value="Canada">Canada</option>
                <option value="United States">United States</option>
            </select></br>

            <label for="phone">Phone - </label>
            <input type="text" name="phone" value="" /><br/>

            <label for="email">Email - </label>
            <input type="text" name="email" value="" /><br/>

            <label for="newsLetterSubscription">Check for Newsletter Subscription</label>
            
            <input type="checkbox" name="newsLetterSubscription" id="newsLetterSubscription"  value="Yes" /><br/>

            <input type="submit" name="submit" value="Submit" />
        </form>
    </body>
</html>
    """;

    # <input type="hidden" name="newsLetterSubscription" value="No" />
def app (environ, start_response):
    response =html;
    if (environ['REQUEST_METHOD'] == "POST"):
        post_env = environ.copy();
        post_env["QUERY_STRING"] = "";

        post = cgi.FieldStorage(
            fp = environ["wsgi.input"],
            environ = post_env,
            keep_blank_values=True
        );

        title = post["title"].value;
        firstName = post["firstName"].value;
        lastName = post["lastName"].value;
        street = post["street"].value;
        city = post["city"].value;
        province = post["province"].value;
        postalCode = post["postalCode"].value;
        country = post["country"].value;
        phone = post["phone"].value;
        email = post["email"].value;
        
        try:
            newsLetterSubscription = post["newsLetterSubscription"].value
            i11 = "checked"
            r3 = ""

        except:
            i11 = ""
            r3 = ""
            #r3 = "<input type='hidden' name='newsLetterSubscription' value='No' />"
            newsLetterSubscription = "No"






        e1 = "<span style='color:red'>*required</span>"
        e2 = "<span style='color:red'>*required</span>"
        e3 = "<span style='color:red'>*required</span>"
        e4 = "<span style='color:red'>*required</span>"
        e5 = "<span style='color:red'>*required</span>"
        e6 = "<span style='color:red'>*required</span>"
        e7 = "<span style='color:red'>*required</span>"
        e8 = "<span style='color:red'>*required</span>"
        e9 = "<span style='color:red'>*required</span>"
        e10 = "<span style='color:red'>*required</span>"
        
        i1 = title
        i1b = title

        i2 = firstName
        i3 = lastName
        i4 = street
        i5 = city
        i6 = province
        i7 = postalCode
        i8 = country
        i8b = country
        
        i9 = phone
        i10 = email
        
        errors = 0

        if(title ==""):
            errors = 1
        else:
            e1=""

        if(firstName ==""):
            errors = 2
        else:
            e2=""

        if(lastName ==""):
            errors = 3
        else:
            e3=""

        if(street ==""):
            errors = 4
        else:
            e4=""

        if(city ==""):
            errors = 5
        else:
            e5=""

        if(province ==""):
            errors = 6
        else:
            e6=""

        if(postalCode ==""):
            errors = 7
        else:
            e7=""

        if(country ==""):
            errors = 8
        else:
            e8=""

        if(phone ==""):
            errors = 9
        else:
            e9=""

        if(email ==""):
            errors = 10
        else:
            e10=""

        

        if (errors != 0):
            response2 = """
            <!DOCTYPE html>
            <html>
                <head>
                    <title> Registration Form  </title>
                </head>
                <body>
                    <form action="" method="POST">
                        <label for="title">Title - </label>
                        <select name="title" id="title">
                            <option value="%s">%s</option>
                            <option value="Mr.">Mr.</option>
                            <option value="Mrs.">Mrs.</option>
                            <option value="Ms.">Ms.</option>
                            <option value="Dr.">Dr.</option>
                        </select>%s</br>
                        <label for="firstName">First Name - </label>
                        <input type="text" name="firstName" value="%s" />%s<br/>
                        <label for="lastName">Last Name - </label>
                        <input type="text" name="lastName" value="%s" />%s<br/>
                        <label for="street">Street - </label>
                        <input type="text" name="street" value="%s" />%s<br/>
                        <label for="city">City - </label>
                        <input type="text" name="city" value="%s" />%s<br/>
                        <label for="province">Province - </label>
                        <input type="text" name="province" value="%s" />%s<br/>
                        <label for="postalCode">Postal Code - </label>
                        <input type="text" name="postalCode" value="%s" />%s<br/>

                        <label for="country">Country - </label>
                        <select name="country" id="country">
                            <option value="%s">%s</option>
                            <option value="Canada">Canada</option>
                            <option value="United States">United States</option>
                        </select>%s</br>

                        <label for="phone">Phone - </label>
                        <input type="text" name="phone" value="%s" />%s<br/>

                        <label for="email">Email - </label>
                        <input type="text" name="email" value="%s" />%s<br/>

                        <label for="newsLetterSubscription">Check for Newsletter Subscription</label>
                        %s
                        <input type="checkbox" name="newsLetterSubscription" id="newsLetterSubscription" %s value="Yes" /><br/>
                        
                        <input type="submit" name="submit" value="Submit" />
                    </form>
                </body>
            </html>
            """

            response = response2 % (i1,i1b,e1,i2,e2,i3,e3,i4,e4,i5,e5,i6,e6,i7,e7,i8,i8b,e8,i9,e9,i10,e10,r3,i11);
        else:

            sql = """INSERT INTO registered_users (title, firstName, lastName, street, city, province, postalCode, country, phone, email, newsLetterSubscription) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            values = [title, firstName, lastName, street, city, province, postalCode, country, phone, email, newsLetterSubscription]
         

            cursor.execute(sql,values)
            db.commit()

            cursor.execute("SELECT * FROM registered_users")
            data = cursor.fetchall()
            
            
            tabledata = """
            <!DOCTYPE html>
            <html>
            <body>
            <table border=1>
                <tr>
                    <th>User Id</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Street</th>
                    <th>City</th>
                    <th>Province</th>
                    <th>Postal Code</th>
                    <th>Country</th>
                    <th>Phone</th>
                    <th>Email</th>
                    <th>New Letter Subscription</th>
                </tr>
                
            """

            for row in data:
                id = row["user_id"]
                firstName = row["firstName"]
                lastName = row["lastName"]
                street = row["street"]
                city = row["city"]
                province = row["province"]
                postalCode = row["postalCode"]
                country = row["country"]
                phone = row["phone"]
                email = row["email"]
                newsLetterSubscription = row["newsLetterSubscription"]

                tabledata += "<tr><td>" + str(id) + "</td><td>" + firstName + "</td><td>" + lastName + "</td><td>" + street + "</td><td>" + city + "</td><td>" + province + "</td><td>" + postalCode + "</td><td>" + country + "</td><td>" + phone + "</td><td>" + email + "</td><td>" + newsLetterSubscription + "</td></tr>"

    

            cursor.close()
            db.close()

            import gc
            gc.collect()

            tabledata += "</table></body></html>"

            response = tabledata



    start_response('200 OK', [('Content-Type', 'text/html')]);
    return [response.encode( )];

if __name__ =='__main__':
    try:
        from wsgiref.simple_server import make_server;
        httpd = make_server('',8080,app);
        print('Serving on port 8080...');
        httpd.serve_forever();
    except KeyboardInterrupt:
        print("Goodbye")