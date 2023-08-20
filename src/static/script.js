$( document ).ready(function() {
    $("#translate").click(function() {
        alert('Start');
        var field1Value = document.getElementById("word").value;

        $.ajax({
            url: '/get_api',
            type: 'GET',
            contentType: 'application/json',
            data: 'user_value='+field1Value,
            success: function(response) {
                alert('entered')
                console.log('response',response);
                $("#result").text(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});


        /*$.get("/get_api", function(data) {
    var dataList = $("#result");
    dataList.empty();
    for(var i=0;i<=data.length;i++){
        word1=data[i];
        dataList.append(word1.definition);
        console.log('word',word1.word);
    }
});
    });
});*/