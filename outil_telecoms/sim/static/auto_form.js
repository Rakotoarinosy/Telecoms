function updatePlafondFields() {
    var forfaitField = document.getElementById("id_forfait");
    var montantPlafondVoixField = document.getElementById("id_montantPlafondVoix");
    var montantPlafondDataField = document.getElementById("id_montantPlafondData");

    var selectedForfait = forfaitField.value;
    console.log(selectedForfait)
    var selectedForfaitOptions = JSON.parse(selectedForfait);
    alert(selectedForfaitOptions);

    if (selectedForfaitOptions) {

        montantPlafondVoixField.value = selectedForfaitOptions.montantPlafondVoix;
        montantPlafondDataField.value = selectedForfaitOptions.montantPlafondData;
        alert(montantPlafondDataField.value);
    } else {
        montantPlafondVoixField.value = "";
        montantPlafondDataField.value = "";
    }
}

var forfaitField = document.getElementById("id_forfait");
if (forfaitField) {
    forfaitField.addEventListener("change", updatePlafondFields);
    updatePlafondFields();
}