(function ($, window, document, undefined) {

  $('#id_place_0').attr('placeholder', 'Select a place');
  $('#id_building_0').attr('placeholder', 'Select a building');

  $('#id_region').on('change', function() {
    $('#id_place_0 option:eq(0)').prop("selected", true);
    $('#id_place_0').val('');
    $('#id_place_0').attr('placeholder', 'Select a place');
    $('#id_building_0 option:eq(0)').prop("selected", true);
    $('#id_building_0').val('');
    $('#id_building_0').attr('placeholder', 'Select a building');

    function newParameters(query) {
      query.region = $('#id_region').val();
    }

    $('#id_place_0').djselectable('option', 'prepareQuery', newParameters);
  });

  // $( "#id_place_0" ).blur(function() {
  //   console.log('CLICKED');
  //   console.log($('#id_place_0').val());

  //   function newParameters(query) {
  //     query.place = $('#id_place_0').val();
  //   }

  //   $('#id_building_0').djselectable('option', 'prepareQuery', newParameters);
  // });

  // $('#building-select a').on('click', function() {

  // });

})(jQuery, this, this.document);
