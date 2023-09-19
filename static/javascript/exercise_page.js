{
    // Get a reference to the video element
    const videoElement = document.getElementById('webcam-element');

    // Check if the browser supports WebRTC
    if ((!navigator.mediaDevices) || (!navigator.mediaDevices.getUserMedia)) {
        console.error('Unfortunately, WebRTC is not supported by this browser.');
    }

    var drawExercises;
    var exerciseList;
    var startExerciseMonitor;
    var exerciseCurIndex    = 0;
    var exerciseMaxSets     = 0;
    
    //  Generates a getter function. Depending on the second
    //  argument, the result may be modified before being
    //  returned.
    function getterFactory(elemId, callback) {
        return function() {
            let exerciseElem        = document.getElementById(elemId);
            if (callback == null) {
                return exerciseElem.innerHTML;
            }
            return callback(exerciseElem.innerHTML);
        };
    }

    function setterFactory(elemId, callback) {
        if (callback == null) {
            return function(value) {
                let exerciseElem        = document.getElementById(elemId);
                exerciseElem.innerHTML  = value;
            };
        }
        return function(value) {
            let exerciseElem        = document.getElementById(elemId);
            exerciseElem.innerHTML  = value;
            callback(exerciseElem, value);
        };
    }

    // Updates the Current Exercise field value.
    var setExerciseName = setterFactory('exer_value');
    // Updates the Repetition # field value.
    var setExerciseReps = setterFactory('rep_value');
    // Updates the numerical count.
    // This function is declared at the very bottom.
    var setCountValue;

    // Returns the exercise name.
    var getExerciseName = getterFactory('exer_value');
    // Returns the Repetition # field value as an integer.
    var getExerciseReps = getterFactory('rep_value', (elem) => parseInt(elem));
    // Returns the numerical count (also an integer).
    var getCountValue   = getterFactory('count_value', (elem) => parseInt(elem));

    // Access the user's camera
    navigator.mediaDevices
        .getUserMedia({ video: true })
        .then(function (stream) {
            // Set the video element's source to the camera stream
            videoElement.srcObject = stream;
            startExerciseMonitor();
            drawExercises();
        })
        .catch(function (error) {
            // Get a reference to the modal element
            alert("Camera access is required for detecting proper execution " +
                "of exercises.");
        });

    drawExercises           = function() {
        var backdropElem    = document.getElementById('exercise_backdrop');
        backdropElem.style.backgroundImage
                            = exerciseList[exerciseCurIndex].img_path;
        exerciseMaxSets     = exerciseList[exerciseCurIndex].sets;
        console.log("Number of sets", exerciseMaxSets);
        setExerciseName(exerciseList[exerciseCurIndex].exercise);
        setExerciseReps(exerciseList[exerciseCurIndex].reps);
        setCountValue(0);
    };

    document.addEventListener('DOMContentLoaded', function () {
        var dataElem    = document.getElementById('data');
        var routineData = dataElem.getAttribute('data-exer-list');

        exerciseList    = JSON.parse(routineData);
        mainElem        = document.getElementById('exercise_main_container');
        cooldownElem    = document.getElementById('exercise_cooldown_container');

        // mainElem.style.display  = "none";
        cooldownElem.style.display  = "none";
    });

    // ===================================================
    //              Exercise Criteria
    // ===================================================

    {
        // Timer object
        var timer;
        // Functions
        var startRestMonitor;
        // Integer variables
        var restTime    = 0;
    
        // Configure this function to suit your needs.
        function getRestPeriod() {
            return 30;
        }

        // Configure this function to suit your needs.
        function exerciseCriteriaFulfilled() {
            return true;
        };

        function redirectToFinishedPage() {
            alert("Sorry, the \"Exercise finished\" page isn't implemented yet.");
            throw Error('404 - Resource not found');
        }

        function enforceRestPeriod() {
            mainElem.style.display      = "none";
            cooldownElem.style.display  = "block";
            restTime                    = getRestPeriod();

            clearInterval(timer);
            startRestMonitor();
            console.log(restTime);
        }
        setCountValue       = setterFactory('count_value', (elem, value) => {
            value           = parseInt(value);
            let repElem     = document.getElementById('rep_value');
            let reps        = parseInt(repElem.innerHTML);
            if (value < reps) {
                return;
            }
            exerciseMaxSets--;
            value           = 0;
            elem.innerHTML  = value;
            if (exerciseMaxSets > 0) {
                enforceRestPeriod();
                return;
            }
            exerciseCurIndex++;
            if (exerciseCurIndex < exerciseList.length) {
                enforceRestPeriod();
                // drawExercises();
            }
            // Redirect to the success page.
        });

        {
            function onMonitorCallback()
            {
                //  The user is finished with his exercises.
                if (exerciseCurIndex >= exerciseList.length) {
                    clearInterval(timer);
                    redirectToFinishedPage();
                    return;
                }
                if (exerciseCriteriaFulfilled()) {
                    setCountValue(getCountValue() + 1);
                }
            }

            function onMonitorRestCallback()
            {
                restTime--;
                if (restTime > 0) {
                    console.log(restTime);
                    return;
                }
                cooldownElem.style.display  = "none";
                mainElem.style.display      = "block";

                clearInterval(timer);
                startExerciseMonitor();
            }

            startExerciseMonitor = function() {
                timer   = setInterval(onMonitorCallback, 250)
            };

            startRestMonitor = function() {
                timer   = setInterval(onMonitorRestCallback, 1000)
            };
        }
    }
}