import webbrowser
f = open('frontend.html','w')
message="""<html>
<head>
<title>seach bar</title>
<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
<div class="wrap">
<div class="seach">
<input type="text" class="searchterm" name="" placeholder="search here">
<button type="submit" class="searchbtn">
<i class="fa fa-search"></i>
</button>
</div>
</div>
</body>
<style>
body{
         background-image: url('https://wp.biologos.org/wp-content/uploads/2019/01/biologos-recommended-books-science-and-faith-1.jpg')
}

.wrap{
     position:absolute;
	 height:60%;
	 width:40%;
	 top:50%;
	 left:50%;
	 transform: translate(-50%,-50%)
	 }
.search{
	 width: 60%;
	 position:relative;
	 }
.searchterm{
     float:left;
     width:70%;
     border:3px solid black;
     padding:11px;
     font-size:19px;
     outline:none;
	 transition: 1s all;
      }
	  
.searchterm:focus{
      color:#00B4CC;
	  border:3px solid #00B4CC ;
}
.searchbtn
{
  position:absolute;
  width:50px;
  height:50px;
  border: 1px solid black;
  background-color: black;
  text-align: center;
  color: #00B4CC;
  cursor: pointer;
  font-size: 20px;
}
	 </style>
	 </html>
"""
f.write(message)
f.close()
webbrowser.open_new_tab('frontend.html')
