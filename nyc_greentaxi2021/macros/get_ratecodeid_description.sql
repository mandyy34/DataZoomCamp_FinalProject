{#
    This macro returns the description of the payment_type 
#}

{% macro get_ratecodeid_description(ratecodeid) -%}

    case {{ dbt.safe_cast("ratecodeid", api.Column.translate_type("integer")) }}  
        when 1 then 'Standard rate'
        when 2 then 'JFK'
        when 3 then 'Newark'
        when 4 then 'Nassau or Westchester'
        when 5 then 'Negotiated fare'
        when 6 then 'Group ride'
    end

{%- endmacro %}