$(document).ready(function() {
    // Fonction de mise à jour des champs
    function updatePlafondFields() {
        var forfaitField = $("#id_forfait");
        var montantPlafondVoixField = $("#id_montantPlafondVoix");
        var montantPlafondDataField = $("#id_montantPlafondData");
        var plafondInterneField = $("#id_plafondInterne");
        var typeSim_idField = $("#id_typeSim_id");
        var selectedForfait = forfaitField.val();
        // Requête AJAX pour récupérer les données du forfait sélectionné
        $.ajax({
            url: "{% url 'get_forfait' %}", // L'URL de la vue Django qui renvoie les détails du forfait
            data: {
                forfait_id: selectedForfait // ID du forfait sélectionné à envoyer au serveur
            },
            dataType: "json",
            success: function(data) {
                if (data) {
                    montantPlafondVoixField.val(data.montantPlafondVoix);
                    montantPlafondDataField.val(data.montantPlafondData);
                    plafondInterneField.val(data.plafondInterne);
                    typeSim_idField.val(data.typeSim_id);
                } else {
                    montantPlafondVoixField.val("");
                    montantPlafondDataField.val("");
                    plafondInterneField.val("");
                    typeSim_idField.val("");
                }
            }
        });
    }
    // Écouteur d'événement pour la modification du champ "forfait"
    var forfaitField = $("#id_forfait");
    forfaitField.on("change", updatePlafondFields);
});
$(document).ready(function() {
    $('#id_collaborateur').on('change', function() {
        var matricule = $(this).val();
        console.log(matricule);
        $.ajax({
            url: "{% url 'get_collaborateur' %}",
            data: {
                'matricule': matricule
            },
            dataType: 'json',
            success: function(data) {
                $('#id_nom').val(data.nom);
                $('#id_prenom').val(data.prenom);
            }
        });
    });
});