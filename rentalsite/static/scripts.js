
$(document).ready(function() {
	 setTimeout(function(){
		$("ul.dj-messages").fadeOut("slow", function () {
		$("ul.dj-messages").remove();
		});
	}, 1000);
	
	$('#login-trigger').click(function(){
		$(this).next('#login-content').slideToggle();
		$(this).toggleClass('active');					
		
		if ($(this).hasClass('active')) 
			$(this).find('span').html('&#x25B2;');
		else 
			$(this).find('span').html('&#x25BC;');
		});
		
		$(".imagelink").colorbox({transition : 'fade', width:"60%", height:"75%"});

	//$('li').hover(function () { $(this).stop().animate({'top':'-50px','height':'100px'}, 1000)}, function () {  $(this).stop().animate({'top':'0px','height':'50px'}, 1000)});
	//$('li').hover( function() { $(this).animate({'height':'200px'}, 2000 }, function() {$(this).animate({'height':'100px'}, 2000 });
   /*var originalBG = $("nav li").css("background-color");

$('nav li').mousemove(function(e) {
	
    x  = e.pageX - this.offsetLeft;
    y  = 1;
    xy = x + " " + y;
	
    bgWebKit = "-webkit-gradient(radial, " + xy + ", 0, " + xy + ", 100, from(rgba(255,255,255,0.8)), to(rgba(255,255,255,0.0))), " + originalBG;
 bgMoz    = "-moz-radial-gradient(" + x + "px " + y + "px 45deg, circle, " + lightColor + " 0%, " + originalBG + " " + gradientSize + "px)";
	alert('boo');
    $(this).css({ background: bgWebKit });
		
}).mouseleave(function() {
	$(this).css({ background: originalBG });
});
	*/

	
	$('.register form').validate({ onkeyup: false,
		rules: {
			username: {
				required: true,
				minlength: 4,
				maxlength: 14,
				remote: "is-available/",
			},
			email: {
				required: true,
				email:true,
			},
			password: {
				required: true,
				minlength: 6,
				maxlength: 14,
			},
			password_repeat: {
				required: true,
				minlength: 6,
				maxlength: 14,
				equalTo: "#id_password",
			}
		},
		messages: {
			username: {
				remote: "Sorry, that username is already in use",
			}
		}
	});
	$('.add-item form').validate({ onkeyup: false,
		rules: {
			name: {
				required: true,
			}
		}
	});
	/*

	jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
		alert("bnoo");
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:)..test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

	/*$('#id_username').rules('add', {required: true, minlength: 2, messages: { required: "Required input", minlength: "Please, at least 5 characters are necessary"} });
		jQuery.validator.addClassRules({ password: { required: true, minlength: 2 }});
*/	
});



/*

				$(function() {
                $('#map_canvas').gmap().bind('init', function(event, map) { 
				$(map).click( function(event) {
		$('#map_canvas').gmap('clear', 'markers');
		$('#map_canvas').gmap('addMarker', {
			'position': event.latLng, 
			'draggable': true, 
			'bounds': false
		}, function(map, marker) {
			$('#dialog').append('<form id="dialog'+marker.__gm_id+'" method="get" action="/" style="display:none;"><p><label for="country">Country</label><input id="country'+marker.__gm_id+'" class="txt" name="country" value=""/></p><p><label for="state">State</label><input id="state'+marker.__gm_id+'" class="txt" name="state" value=""/></p><p><label for="address">Address</label><input id="address'+marker.__gm_id+'" class="txt" name="address" value=""/></p><p><label for="comment">Comment</label><textarea id="comment" class="txt" name="comment" cols="40" rows="5"></textarea></p></form>');
			findLocation(marker.getPosition(), marker);
		})
	});
});

function findLocation(location, marker) {
	$('#map_canvas').gmap('search', {'location': location}, function(results, status) {
		if ( status === 'OK' ) {
			$.each(results[0].address_components, function(i,v) {
				if ( v.types[0] == "administrative_area_level_1" || 
					 v.types[0] == "administrative_area_level_2" ) {
					$('#state'+marker.__gm_id).val(v.long_name);
				} else if ( v.types[0] == "country") {
					$('#country'+marker.__gm_id).val(v.long_name);
				}
			});
			marker.setTitle(results[0].formatted_address);
			$('#address'+marker.__gm_id).val(results[0].formatted_address);
			openDialog(marker);
		}
	});
}

function openDialog(marker) {
	$('#dialog'+marker.__gm_id).dialog({'modal':true, 'title': 'Edit and save point', 'buttons': { 
		"Remove": function() {
			$(this).dialog( "close" );
			marker.setMap(null);
		},
		"Save": function() {
			$(this).dialog( "close" );
		}
	}});
}

*/