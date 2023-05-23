$(document).ready(function() {
    // Masquer les champs montantPlafondVoix et montantPlafondData au chargement de la page
    $('.voix').hide();
    $('.data').hide();
    $('.voix-data').hide();

    // Écouter l'événement de changement de valeur du champ "Type de SIM"
    $('#id_typeSim').change(function() {
        var selectedType = $(this).children("option:selected").attr('class');

        // Masquer tous les champs
        $('.voix').hide();
        $('.data').hide();
        $('.voix-data').hide();

        // Afficher les champs en fonction du type sélectionné
        if (selectedType === 'voix') {
            $('.voix').show();
        } else if (selectedType === 'data') {
            $('.data').show();
        } else if (selectedType === 'voix-data') {
            $('.voix').show();
            $('.data').show();
        }
    });
});