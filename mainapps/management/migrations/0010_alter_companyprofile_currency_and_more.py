# Generated by Django 4.2.13 on 2024-06-01 11:49

from django.db import migrations, models
import iso4217
import mainapps.inventory.helpers.field_validators


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_alter_companyprofile_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='currency',
            field=models.CharField(blank=True, choices=[(iso4217.Currency['afn'], 'AFN'), (iso4217.Currency['eur'], 'EUR'), (iso4217.Currency['all'], 'ALL'), (iso4217.Currency['dzd'], 'DZD'), (iso4217.Currency['usd'], 'USD'), (iso4217.Currency['aoa'], 'AOA'), (iso4217.Currency['xcd'], 'XCD'), (iso4217.Currency['ars'], 'ARS'), (iso4217.Currency['amd'], 'AMD'), (iso4217.Currency['awg'], 'AWG'), (iso4217.Currency['aud'], 'AUD'), (iso4217.Currency['azn'], 'AZN'), (iso4217.Currency['bsd'], 'BSD'), (iso4217.Currency['bhd'], 'BHD'), (iso4217.Currency['bdt'], 'BDT'), (iso4217.Currency['bbd'], 'BBD'), (iso4217.Currency['byn'], 'BYN'), (iso4217.Currency['bzd'], 'BZD'), (iso4217.Currency['xof'], 'XOF'), (iso4217.Currency['bmd'], 'BMD'), (iso4217.Currency['inr'], 'INR'), (iso4217.Currency['btn'], 'BTN'), (iso4217.Currency['bob'], 'BOB'), (iso4217.Currency['bov'], 'BOV'), (iso4217.Currency['bam'], 'BAM'), (iso4217.Currency['bwp'], 'BWP'), (iso4217.Currency['nok'], 'NOK'), (iso4217.Currency['brl'], 'BRL'), (iso4217.Currency['bnd'], 'BND'), (iso4217.Currency['bgn'], 'BGN'), (iso4217.Currency['bif'], 'BIF'), (iso4217.Currency['cve'], 'CVE'), (iso4217.Currency['khr'], 'KHR'), (iso4217.Currency['xaf'], 'XAF'), (iso4217.Currency['cad'], 'CAD'), (iso4217.Currency['kyd'], 'KYD'), (iso4217.Currency['clp'], 'CLP'), (iso4217.Currency['clf'], 'CLF'), (iso4217.Currency['cny'], 'CNY'), (iso4217.Currency['cop'], 'COP'), (iso4217.Currency['cou'], 'COU'), (iso4217.Currency['kmf'], 'KMF'), (iso4217.Currency['cdf'], 'CDF'), (iso4217.Currency['nzd'], 'NZD'), (iso4217.Currency['crc'], 'CRC'), (iso4217.Currency['hrk'], 'HRK'), (iso4217.Currency['cup'], 'CUP'), (iso4217.Currency['cuc'], 'CUC'), (iso4217.Currency['ang'], 'ANG'), (iso4217.Currency['czk'], 'CZK'), (iso4217.Currency['dkk'], 'DKK'), (iso4217.Currency['djf'], 'DJF'), (iso4217.Currency['dop'], 'DOP'), (iso4217.Currency['egp'], 'EGP'), (iso4217.Currency['svc'], 'SVC'), (iso4217.Currency['ern'], 'ERN'), (iso4217.Currency['szl'], 'SZL'), (iso4217.Currency['etb'], 'ETB'), (iso4217.Currency['fkp'], 'FKP'), (iso4217.Currency['fjd'], 'FJD'), (iso4217.Currency['xpf'], 'XPF'), (iso4217.Currency['gmd'], 'GMD'), (iso4217.Currency['gel'], 'GEL'), (iso4217.Currency['ghs'], 'GHS'), (iso4217.Currency['gip'], 'GIP'), (iso4217.Currency['gtq'], 'GTQ'), (iso4217.Currency['gbp'], 'GBP'), (iso4217.Currency['gnf'], 'GNF'), (iso4217.Currency['gyd'], 'GYD'), (iso4217.Currency['htg'], 'HTG'), (iso4217.Currency['hnl'], 'HNL'), (iso4217.Currency['hkd'], 'HKD'), (iso4217.Currency['huf'], 'HUF'), (iso4217.Currency['isk'], 'ISK'), (iso4217.Currency['idr'], 'IDR'), (iso4217.Currency['xdr'], 'XDR'), (iso4217.Currency['irr'], 'IRR'), (iso4217.Currency['iqd'], 'IQD'), (iso4217.Currency['ils'], 'ILS'), (iso4217.Currency['jmd'], 'JMD'), (iso4217.Currency['jpy'], 'JPY'), (iso4217.Currency['jod'], 'JOD'), (iso4217.Currency['kzt'], 'KZT'), (iso4217.Currency['kes'], 'KES'), (iso4217.Currency['kpw'], 'KPW'), (iso4217.Currency['krw'], 'KRW'), (iso4217.Currency['kwd'], 'KWD'), (iso4217.Currency['kgs'], 'KGS'), (iso4217.Currency['lak'], 'LAK'), (iso4217.Currency['lbp'], 'LBP'), (iso4217.Currency['lsl'], 'LSL'), (iso4217.Currency['zar'], 'ZAR'), (iso4217.Currency['lrd'], 'LRD'), (iso4217.Currency['lyd'], 'LYD'), (iso4217.Currency['chf'], 'CHF'), (iso4217.Currency['mop'], 'MOP'), (iso4217.Currency['mkd'], 'MKD'), (iso4217.Currency['mga'], 'MGA'), (iso4217.Currency['mwk'], 'MWK'), (iso4217.Currency['myr'], 'MYR'), (iso4217.Currency['mvr'], 'MVR'), (iso4217.Currency['mru'], 'MRU'), (iso4217.Currency['mur'], 'MUR'), (iso4217.Currency['xua'], 'XUA'), (iso4217.Currency['mxn'], 'MXN'), (iso4217.Currency['mxv'], 'MXV'), (iso4217.Currency['mdl'], 'MDL'), (iso4217.Currency['mnt'], 'MNT'), (iso4217.Currency['mad'], 'MAD'), (iso4217.Currency['mzn'], 'MZN'), (iso4217.Currency['mmk'], 'MMK'), (iso4217.Currency['nad'], 'NAD'), (iso4217.Currency['npr'], 'NPR'), (iso4217.Currency['nio'], 'NIO'), (iso4217.Currency['ngn'], 'NGN'), (iso4217.Currency['omr'], 'OMR'), (iso4217.Currency['pkr'], 'PKR'), (iso4217.Currency['pab'], 'PAB'), (iso4217.Currency['pgk'], 'PGK'), (iso4217.Currency['pyg'], 'PYG'), (iso4217.Currency['pen'], 'PEN'), (iso4217.Currency['php'], 'PHP'), (iso4217.Currency['pln'], 'PLN'), (iso4217.Currency['qar'], 'QAR'), (iso4217.Currency['ron'], 'RON'), (iso4217.Currency['rub'], 'RUB'), (iso4217.Currency['rwf'], 'RWF'), (iso4217.Currency['shp'], 'SHP'), (iso4217.Currency['wst'], 'WST'), (iso4217.Currency['stn'], 'STN'), (iso4217.Currency['sar'], 'SAR'), (iso4217.Currency['rsd'], 'RSD'), (iso4217.Currency['scr'], 'SCR'), (iso4217.Currency['sll'], 'SLL'), (iso4217.Currency['sle'], 'SLE'), (iso4217.Currency['sgd'], 'SGD'), (iso4217.Currency['xsu'], 'XSU'), (iso4217.Currency['sbd'], 'SBD'), (iso4217.Currency['sos'], 'SOS'), (iso4217.Currency['ssp'], 'SSP'), (iso4217.Currency['lkr'], 'LKR'), (iso4217.Currency['sdg'], 'SDG'), (iso4217.Currency['srd'], 'SRD'), (iso4217.Currency['sek'], 'SEK'), (iso4217.Currency['che'], 'CHE'), (iso4217.Currency['chw'], 'CHW'), (iso4217.Currency['syp'], 'SYP'), (iso4217.Currency['twd'], 'TWD'), (iso4217.Currency['tjs'], 'TJS'), (iso4217.Currency['tzs'], 'TZS'), (iso4217.Currency['thb'], 'THB'), (iso4217.Currency['top'], 'TOP'), (iso4217.Currency['ttd'], 'TTD'), (iso4217.Currency['tnd'], 'TND'), (iso4217.Currency['try'], 'TRY'), (iso4217.Currency['tmt'], 'TMT'), (iso4217.Currency['ugx'], 'UGX'), (iso4217.Currency['uah'], 'UAH'), (iso4217.Currency['aed'], 'AED'), (iso4217.Currency['usn'], 'USN'), (iso4217.Currency['uyu'], 'UYU'), (iso4217.Currency['uyi'], 'UYI'), (iso4217.Currency['uyw'], 'UYW'), (iso4217.Currency['uzs'], 'UZS'), (iso4217.Currency['vuv'], 'VUV'), (iso4217.Currency['ves'], 'VES'), (iso4217.Currency['ved'], 'VED'), (iso4217.Currency['vnd'], 'VND'), (iso4217.Currency['yer'], 'YER'), (iso4217.Currency['zmw'], 'ZMW'), (iso4217.Currency['zwl'], 'ZWL'), (iso4217.Currency['xba'], 'XBA'), (iso4217.Currency['xbb'], 'XBB'), (iso4217.Currency['xbc'], 'XBC'), (iso4217.Currency['xbd'], 'XBD'), (iso4217.Currency['xts'], 'XTS'), (iso4217.Currency['xxx'], 'XXX'), (iso4217.Currency['xau'], 'XAU'), (iso4217.Currency['xpd'], 'XPD'), (iso4217.Currency['xpt'], 'XPT'), (iso4217.Currency['xag'], 'XAG')], default='USD', help_text='Set company default currency', max_length=12, validators=[mainapps.inventory.helpers.field_validators.validate_currency_code], verbose_name='Base Currency'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='unique_id',
            field=models.CharField(default='924174166692846', editable=False, max_length=15, unique=True),
        ),
    ]