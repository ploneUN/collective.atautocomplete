jQuery(document).ready( function() {
    var autocompletefields = jQuery('textarea.atautocomplete');
    autocompletefields.each( function(itemindex) {
        var item = autocompletefields.eq(itemindex);

        // load json data
        var url = jQuery("input[name=" + item.attr('id') + "_atautocomplete_url]").eq(0).val();
        jQuery.getJSON(url, function(data) {
            item.autocomplete(data, {
                multiple: true,
                mustMatch: false,
                autoFill: true
            });
        });
    });
} );
