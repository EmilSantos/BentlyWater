$(document).ready(function() {
    $(".clickable-row").click(function() {

        // Remove the highlight from all rows
        $(".clickable-row").removeClass("selected-row");
        
        // Highlight the clicked row
        $(this).addClass("selected-row");
        const url = $(this).data("href");
        $.ajax({
            url: url,
            method: "GET",
            dataType: 'json',
            success: function(data) {
                $("#detail_permit").text(data.permit_num);
                $("#detail_basin").text(data.basin);
                $("#detail_cert_status").text(data.cert_status);
                $("#detail_owner").text(data.owner_of_record);
                $("#detail_priority_date").text(data.priority_date);

                $("#detail_cfs").text(data.cfs);
                $("#detail_duty_af").text(data.duty_af);
                $("#detail_poc_due").text(data.poc_due);
                $("#detail_pbu_due").text(data.pbu_due);
                $("#detail_use").text(data.use);
                $("#detail_source").text(data.source);
                $("#detail_remarks").text(data.remarks);
                $("#detail_sale_value").text(data.sale_value);
                $("#detail_potential_valuesr").text(data.potential_values);

                $("#detail_pod_1").text(data.pod_1);
                $("#detail_pod_2").text(data.pod_2);
                $("#detail_pod_3").text(data.pod_3);
                $("#detail_pod_4").text(data.pod_4);
                $("#detail_pod_5").text(data.pod_5);

                $("#detail_unit_acres").text(data.unit_acres);
                $("#detail_unit_sheep").text(data.unit_sheep);
                $("#detail_unit_lamb").text(data.unit_lamb);
                $("#detail_unit_cattle").text(data.unit_cattle);
                $("#detail_unit_horses").text(data.unit_horses);
                $("#detail_unit_other").text(data.unit_other);

                $("#detail_created_by").text(data.created_by);
                $("#detail_modified_by").text(data.modified_by);
                $("#detail_create_date").text(data.create_date);
                $("#detail_modify_date").text(data.modify_date);
            },
            error: function(error) {
                console.error("Error fetching details", error);
            }
        });
    });
});



document.addEventListener("DOMContentLoaded", function() {
    let clickableRows = document.querySelectorAll(".clickable-row");

    clickableRows.forEach(row => {
        row.addEventListener("click", function() {
            let url = this.getAttribute("data-href");
            if (url) {
                window.location.href = url;
            }
        });
    });
});


$(document).ready(function(){
    window.setTimeout(function() {
        $(".alert").fadeTo(500, 0).slideUp(500, function(){
            $(this).remove(); 
        });
    }, 3000);
});
