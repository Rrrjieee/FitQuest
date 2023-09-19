{
    var selectedIndex   = 0;
    var userIndex       = 0;
    var startButton     = document.getElementById('routine_start');

    function createButtonEventSubscriber(elemId, index) {
        var button              = document.getElementById(elemId);
        var callback            = function() {
            var prevIndex       = selectedIndex;
            selectedIndex       = index;
            if (prevIndex == selectedIndex) {
                button.blur();
                selectedIndex       = 0;
                startButton.href    = "";
            } else {
                startButton.href    = "/user_id=" + userIndex + "/ready"
            }
            console.log("Currently selected option:", selectedIndex);
        };
        button.addEventListener("click", callback);
    }

    createButtonEventSubscriber("routine_option_1", 1);
    createButtonEventSubscriber("routine_option_2", 2);
    startButton.addEventListener("click", () => {
        if (selectedIndex == 0) {
            alert('Please select a routine.');
            return;
        }
        var streamBody  = {
            "method": "premade",
            "index": selectedIndex - 1
        }
        fetch('/req_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(streamBody),
        })
        window.location.href    = '/user_id=' + userIndex + '/ready';
    })

    
    // ===================================================
    // ===================================================
    document.addEventListener('DOMContentLoaded', function () {
        // Retrieve the data from the 'data' div element
        var dataElement = document.getElementById('data');
        userIndex       = dataElement.getAttribute('data-id');
        var routineJSON = dataElement.getAttribute('data-routine');
        var descJSON    = dataElement.getAttribute('data-routine-desc');

        // Parse the data as JSON
        var routineData = JSON.parse(routineJSON);
        var descData    = JSON.parse(descJSON);
        
        // Change the background image of the icons within the routine option cabaret.
        // Now you can access the values in the 'data' JavaScript object
        for (let i = 1; i < 3; i++) {
            var optionElem      = document.getElementById('option-' + i);
            var cabaret         = optionElem.getElementsByClassName('routine_img_cabaret')[0];
            var descElem        = optionElem.getElementsByClassName('routine_desc_container')[0];
            //  Update routine appearance
            for (let j = 0; j < cabaret.children.length; j++) {
                //  Create background image:
                childElem       = cabaret.children[j].children[0];
                childElem.style.backgroundImage = routineData[i-1][j].img_path;

                //  Set Repetitions text.
                childElem       = cabaret.children[j].children[1];
                childElem.innerText = "Repetitions: " + routineData[i-1][j].reps;

                //  Set Number of sets text.
                childElem       = cabaret.children[j].children[2];
                if (routineData[i-1][j].sets > 1) {
                    childElem.innerText = "Sets #: " + routineData[i-1][j].sets;
                } else {
                    childElem.innerText = "Sets #: 1";
                }
            };
            //  Update description.
            descElem.children[1].innerText  = descData[i-1];
        }
    });
}