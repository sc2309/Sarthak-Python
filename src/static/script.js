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
                //console.log('response',response);
                //$("#result").text(response);
                
                const indexA = 0;
                const indexB = 2;
                const indexC = 2;
                const indexD = 1;
                const indexE = 0;
                const indexF = 1;

                for (let a = 0; a < response.length; a++) {
                    if (a === indexA) {
                        for (let b = 0; b < response[a].length; b++) {
                            if (b === indexB) {
                                for (let c = 0; c < response[a][b].length; c++) {
                                    if (c === indexC) {
                                        for (let d = 0; d < response[a][b][c].length; d++) {
                                            if (d === indexD) {
                                                for (let e = 0; e < respo2nse[a][b][c][d].length; e++) {
                                                    if (e === indexE) {
                                                        for (let f = 0; f < response[a][b][c][d][e].length; f++) {
                                                            if (f === indexF) {
                                                                const WordMeaning = response[a][b][c][d][e][f][g];
                                                                console.log("response:", WordMeaning);
                                                                break;
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

                $("#result").text(WordMeaning);
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