(function ($, window, document, undefined) {

  $('#id_region').on('change', function() {
    $('#id_place_0 option:eq(0)').prop("selected", true);
    $('#id_place_0').val('Select a place');
    function newParameters(query) {
      query.region = $('#id_region').val();
    }

    $('#id_place_0').djselectable('option', 'prepareQuery', newParameters);
  });

  $('#id_place_0').on('change', function() {
    $('#id_building_0 option:eq(0)').prop("selected", true);
    $('#id_building_0').val('Select a building');
    function newParameters(query) {
      query.region = $('#id_place_0').val();
    }

    $('#id_building_0').djselectable('option', 'prepareQuery', newParameters);
  });

})(jQuery, this, this.document);
