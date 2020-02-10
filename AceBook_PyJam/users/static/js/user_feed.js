$(function(){//Wait for page to be ready
  $('#hamburger').click(function(){
    $('.nav').css('margin-left', '0');
    $('.navoverlay').css('opacity', '1');
    $('.navoverlay').css('z-index', '60');
    $('.navoverlay').click(function(){
      $('.navoverlay').css('opacity', '0');
      $('.navoverlay').css('z-index', '-1');
      $('.nav').css('margin-left', '-100%');
    })
  })
})

$('#plus').click(function(){
  $('.navoverlay').css('z-index', '100');
  $('.navoverlay').css('opacity', '1');
  $('#activityform').css('height', '500px');
  $('#activityform').css('padding', '20px');
  $('#activityform').css('opacity', '1');
  $('#activityform').css('z-index', '110');
  $('.navoverlay').click(function(){
      $('.navoverlay').css('z-index', '-1');
      $('.navoverlay').css('opacity', '0');
    	$('#activityform').css('height', '0px');
      $('#activityform').css('padding', '0px');
      $('#activityform').css('opacity', '0');
      $('#activityform').css('z-index', '-2');
	})
})


$(function(){//Wait for page to be ready
  var filtersOpen = false;
  $('#option').click(function(){
    $('.blog-post').css('display', 'block');
  })
  $('#settings').click(function(){
    if(filtersOpen){
      //Move Filter Window Off screen
     $('.filters').css('right','-100%');
      filtersOpen = false;//set the boolean to false
    }else{
    $('.filters').css('right', '0px');
    filtersOpen = true; //set the boolean to true
    }
  })
})

	var blogOpen = false;
  $('#blog-filter').click(function(){
    if(!blogOpen){
   		$('.blog').css('height', '0');
      $('.blog').css('margin-bottom', '0');
      $('#blog-filter').css('color', '#DEDEDE');
      blogOpen = true;
   }else{
   		$('.blog').css('height', '100px');
      $('.blog').css('margin-bottom', '10px');
      $('#blog-filter').css('color', '#222');
     blogOpen = false;
   }
  });


	var portfolioOpen = false;
  $('#portfolio-filter').click(function(){
    if(!portfolioOpen){
   		$('.portfolio').css('height', '0');
      $('.portfolio').css('margin-bottom', '0px');
      $('#portfolio-filter').css('color', '#DEDEDE');
      portfolioOpen = true;
   }else{
   		$('.portfolio').css('height', '100px');
      $('.portfolio').css('margin-bottom', '10px');
      $('#portfolio-filter').css('color', '#222');
     portfolioOpen = false;
   }
  });
var data =[];   //A variable to keep track of the data coming from Firebase
var ref = new Firebase("https://yikesitsmikes.firebaseio.com/activities");
 ref.on("value", function(snapshot){ //Listen to data updates from firebase
		console.log(snapshot.val());
    data = snapshot.val(); //When data updates at Firebase, put it in the data variable
 })


  //Make a template from the HTML
  //<% if (obj.type) { %><%= type %><% } %>
  var compiled = _.template(
    '<div class="feed-item <% if (obj.type) { %><%= type %><% } %> <% if (obj.firebase) { %>firebase<% } %>"><div class="icon-holder col-1-5"><div class="icon"></div></div><div class="text-holder col-3-5"><div class="feed-title"><%= title %></div><div class="feed-description"><%= description %></div> </div><div class="post-options-holder"><div class= "tools"><i class="fa fa-ellipsis-v" id="postsettings"></i></div></div> <div class="col-1-5"></div></div>');


  var ref = new Firebase("https://yikesitsmikes.firebaseio.com/activities");

  ref.on("value", function(snapshot){
    console.log(snapshot.val());
    var data = snapshot.val();
    $('.firebase').remove();
    for(i=0; i<data.length;i++){
      data[i].firebase = true;
      var text = compiled(data[i]);
      $('.feed').append(text);
    }
  })




//================== FORM =========================

$(function(){

var data =[];   //Make a variable to keep track of the data coming from Firebase
var ref = new Firebase("https://yikesitsmikes.firebaseio.com/activities");
 ref.on("value", function(snapshot){ //Listen to data updates from firebase
		console.log(snapshot.val());
    data = snapshot.val(); //Dhen data updates at Firebase, put it in the data variable
 })


//Submit Function
$('#newActivity').submit(function(event){
  var $form = $(this);

  $form.find("#saveForm").prop('disabled', true); //make the submit disabled

  //get the actual values that we will send to firebase
  var titleToSend = $('#activityTitle').val();
  var descToSend = $('#activityDescription').val();
  var categoryToSend = $('#activityCatagory').val();

  var newActivity = { //take the values from the form, and put them in an object
      "description": descToSend,
      "title":titleToSend,
      "type": categoryToSend
  }
  data.push(newActivity); //Put the new object into the data array
  console.log(data);
  ref.set(data, function(err){ //Send the new data to Firebase
    if(err){
      console.log(err);
      alert("Error -10");
    }
    else{
      alert("Activity Successfully Submitted!");
    }
  });
  return false;
})


 $("#registerForm").click(function(event){ //Clicked the Register Button

    var $form = $(this);
    $form.find('#registerForm').prop('disabled', true); //Disable the button

    var login = $("#loginInput").val();//get the value of the login email
    var pass = $("#pwField").val();//get the value of the password

    reg.createUser({ //Create User from data
      email: login,
      password: pass
    }, function(error, userData){
      if(error){
        alert("Already Registered or Error with Form");
      }else{
        alert("You registered "+userData.uid);
      }
    })
	return false;
 }); //End Register Button



 $("#finalloginForm").click(function(event){ //Clicked the login Button

    var $form = $(this);
    $form.find('#registerForm').prop('disabled', true); //Disable the button

    var login = $("#loginInput").val();//get the value of the login email
    var pass = $("#pwField").val();//get the value of the password

    var reg = new Firebase("https://yikesitsmikes.firebaseio.com");
    reg.authWithPassword({
      email: login,
      password: pass
    },function(error, user){
      if(error){
        alert("Email and password combination do not exist")
      }else{
        alert("Logged in with "+user.uid);
         $('#formHolder').css('display', 'block');
      }
    })
  return false;  location.reload(forceGet);
 });





  ////Detect Authication state
  var reg = new Firebase("https://yikesitsmikes.firebaseio.com");
  reg.onAuth(function(authData){
    console.log("info on authentication");
    console.log(reg);

    if(authData){ //If Logged in

      console.log("You are logged in!");
      $('#register').css('display', 'none');
      $('#loginform').css('display', 'none');
      $('#formHolder').css('width', '100%');
      $('#spacer').css('height', '0');
      $('#logoutbut').css('display', 'block');

    }else{
      console.log("You are not logged in");
      $('#logoutbut').css('display', 'none');
    }
  })



  //Logout Function
  $('#logout').click(function(event){
  	console.log("Logging out");
  	var reg = new Firebase("https://yikesitsmikes.firebaseio.com");
 	  reg.unauth();
    alert("You have logged out.")
  })
})


  
