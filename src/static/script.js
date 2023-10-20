$( document ).ready(function() {
    $("#translate").click(function() {
        var field1Value = document.getElementById("word").value;

        $.ajax({
            url: '/get_api',
            type: 'GET',
            contentType: 'application/json',
            data: 'user_value='+field1Value,
            success: function(response) {
                //console.log('meaning',response);
                //$("#result").text(response);

                    if (response.length > 0 && response[0].meanings.length > 0 && response[0].meanings[0].definitions.length > 0) {
                        var WordMeaning = response[0].meanings[0].definitions[0].definition;
                        console.log('meaning', WordMeaning);
                        $("#result").text(WordMeaning);
                    }
                    else {
                        console.log('No definitions found in the response');
                        $("#result").text('No definitions found');
                    }
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
});


console.log(WordMeaning)//'response',WordMeaning)
*/