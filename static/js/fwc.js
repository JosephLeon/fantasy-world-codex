(function ($, window, document, undefined) {

  $('#id_region').on('change', function() {
    $('#id_place_0 option:eq(0)').prop("selected", true);
    function newParameters(query) {
      query.region = $('#id_region').val();
    }

    $('#id_place_0').djselectable('option', 'prepareQuery', newParameters);
  });

})(jQuery, this, this.document);
