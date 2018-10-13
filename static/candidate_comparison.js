
$(document)
    .ready(function() {
        $('.ui.accordion')
            .accordion({
                selector: {
                    trigger: '.title'
                }
            });
    
        // Send event when an outbound link is clicked.
        $('a').click(function(event) {
            gtag('event', 'click', {
                 'event_category': 'Outbound Link',
                 'event_label': $.trim($(this).text()),
                 'transport_type': 'beacon'
            });
        });

        // Send an event when a section header is clicked.
        $('.title').click(function(event) {
            gtag('event', 'click', {
                'event_category': 'Section Expansion',
                'event_label': this.id
            });
        });
    })
;


