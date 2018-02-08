import cgi, cgitb
cgitb.enable()

def load():
    print 'Content-type: text/html\n\n'
    first = """
    <!DOCTYPE html>
    <html>

        <head>
            <title>JaJaS</title>

            <script type="text/javascript">
                if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
                    window.location.replace("noMobile.html");
                }
            </script>

            <link href="base.css" rel="stylesheet" type="text/css">
            <link href="indexstyle.css" rel="stylesheet" type="text/css">

            <meta charset="UTF-8">

            <meta name="description" content="Garden Shop">

            <meta name="author" content="Joan Chirinos">
            <meta name="author" content="Aaron Li">
            <meta name="author" content="Johnny Wong">

            <meta name="viewport" content="width=device-width, initial-scale-1.0">

            <!-- Linking to Google's jQuery -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        </head>

        <body>

            <div class="titleWrapper">
                <center><h1><a href="index.html" class="title">JaJaS Gardening Shop</a></h1></center>
            </div>
            <div class="navBarWrapper">
                <div class="dropdown">
                    <button class="dropbtn">Categories</button>
                    <div class="dropdown-content">
                        <a href="#">Add</a>
                        <a href="#">Categories</a>
                        <a href="#">Here</a>
                    </div>
                </div>
                <div class="searchBar">
                    <form action="/search.py">
                        Search:&nbsp;
                        <input class="searchBox" type="text" name="searchInput" placeholder="Search terms"/>
                        <input type="submit" name="submit" value="Search!">
                    </form>
                </div>
            </div>"""
    second = """
        </body>

    </html>
    """
    print first + second
    
load();