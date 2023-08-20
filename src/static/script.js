$( document ).ready(function() {
    $("#translate").click(function() {
        alert('Start');
        var field1Value = document.getElementById("word").value;

        fetch('/get_api', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ htmlValue: field1Value })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
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