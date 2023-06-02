function updateChampsAffiches() {
    var selectBox = document.getElementById('id_typeSim');
    var montantPlafondVoix = document.getElementById('id_montantPlafondVoix');
    var montantPlafondData = document.getElementById('id_montantPlafondData');

    switch (selectBox.value) {
        case "1":
            montantPlafondVoix.style.display = 'none';
            montantPlafondData.style.display = 'block';
            break;
        case "2":
            montantPlafondVoix.style.display = 'block';
            montantPlafondData.style.display = 'none';
            break;
        default:
            montantPlafondVoix.style.display = 'block';
            montantPlafondData.style.display = 'block';
    }
}