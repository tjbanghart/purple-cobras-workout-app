$("#myTable").hide();
$("#addWorkouts").hide();
$("#backExercise").hide();

$("#workouts").click(function(){
	$("#myTable").toggle();
	$("#addWorkouts").hide();
	$("#backExercise").hide();
});

$("#add").on("click", function(){
	$("#addWorkouts").toggle();
	$("#addButtons").show();
	$("#myTable").hide();
	$("#createW").hide();
	$("#searchW").hide()
	$("#userStats").hide();
	$("#successMessage").hide();
	$("#backExercise").hide();
});

$("#addW").click(function(event){
	$("#createW").show();
	$("#addButtons").hide();
});

$("#sW").click(function(event){
	$("#userStats").show();
	$("#addButtons").hide();
});


$("#contB").click(function(event){
	$("#userStats").hide();
	$("#searchW").show();
});

$("#contB2").click(function(event){
	$("#searchW").hide();
	$("#successMessage").show();
	// uncheck the box
	 $("#backWorkout").prop("checked", false);
	// add an exercise
	$("table").append("<tr class='x'><td class='delete'><i class='fa fa-trash'></i></td><td>Back</td><td>Bend-over rows</td><td>20 min</td><td><button type='button' class='btn btn-info btn-xs'>see exercise</button></td></tr>")
});

// remove items
$("#myTable").on("click", ".delete", function(event){
	$(this).parent().fadeOut(500, function(){
		$(this).remove();
	});
	event.stopPropagation();
});

$("#createB").click(function(event){
	$("#createW").hide();
	$("#successMessage").show();
	// add an exercise
	var targetMuscle = $("#targetMuscle").val();
	var exercise = $("#exercise").val();
	var duration = $("#duration").val();
		$("#targetMuscle").val("");
		$("#exercise").val("");
		$("#duration").val("");
	$("table").append("<tr class='x'><td class='delete'><i class='fa fa-trash'></i></td><td>" + targetMuscle + "</td><td>" + exercise + "</td><td>" + duration + "</td><td><button type='button' class='btn btn-info btn-xs'>see exercise</button></td></tr>")
});

$("#backDetails").click(function(event){
	$("#backExercise").show();
	$("#myTable").hide();
});


$("#btnGoBackWorkouts").click(function(event){
	$("#backExercise").hide();
	$("#myTable").show();
});
