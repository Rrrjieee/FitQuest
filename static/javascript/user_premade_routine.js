{
    var lastSelectedElem    = null;
    var lastSelectedIndex   = 0;

    function createButtonEventSubscriber(elemId, index) {
        var callback        = function() {
            lastSelectedElem    = elemId;
            lastSelectedIndex   = index;
            console.log("Last selected element:", elemId)
        };
        var button          = document.getElementById(elemId);
        button.addEventListener("click", callback);
    }

    createButtonEventSubscriber("routine_option_1");
    createButtonEventSubscriber("routine_option_2");
}