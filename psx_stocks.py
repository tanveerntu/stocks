# pip install streamlit plotly

#pip install psx-data-reader

from typing import ClassVar
from psx import stocks, tickers 
import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly
from prophet.plot import plot_plotly
from plotly import graph_objs as go

#START = "2015-01-01" #date from which to start data
#TODAY = date.today().strftime("%Y-%m-%d")  #day till getting data; #strftime = string format time

st.set_page_config(page_title="Forecasting Pakistani Stocks",
                   page_icon=":bar_chart:"   #https://www.webfx.com/tools/emoji-cheat-sheet/

)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
         header {visibility: hidden;}
       """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title('Forecasting Pakistani Stocks')

st.subheader('Companies Listed in PSX')

#to show progress
import time

with st.spinner('Gathering the list...'):
   time.sleep(4)
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)


##

df_tickers = tickers()
#see tickers of all companies listed in psx

#df_tickers # to show dataframe

df_tickers = df_tickers[["symbol", "name", "sectorName"]]

df_tickers

#
#to download tickers dataframe as csv 
@st.cache
def convert_df(df_tickers):
   return df_tickers.to_csv().encode('utf-8')


csv = convert_df(df_tickers)

st.download_button(
   "Press to Download above data as .csv, if you require.",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
#
st.info('Note: Download is not required for forecasting')

import datetime 
#data = stocks("ILP", start=datetime.date(2019, 1, 1), end=datetime.date.today())
#data 
#data1 = data.reset_index(inplace=True) #to put dates in first colums of dataframe
#data1 

#stock_name = ('SILK', 'PACE') #codes on yahoo finance site of diff. companies, curreny etc.
#selected_stock = st.selectbox('Select dataset for prediction', stock_name)

#df = stocks("SILK", start=datetime.date(2020, 1, 1), end=datetime.date.today())
#df 

st.subheader('Select No. of Future Years for Forecasting')
st.info('1 year is selected by default')

n_years = st.slider('Select', 1, 4)
period = n_years * 365

st.subheader('Select a Stock Option below')
st.info('ILP, Interloop is selected by default')

option = st.selectbox(
    'Select',
    (
        'KELSC5',
        'JSBLTFC2',
        'AGSILSC',
        'AKBLTFC6',
        'AKBLTFC7',
        'ANLTFC2',
        'BAFLTFC6',
        'BAFLTFC7',
        'BIPLSC',
        'BYCOSC',
        'EPCLSC',
        'FATIMASC',
        'HBLTFC2',
        'HUBCSC2',
        'HUBCSC4',
        'HUBPHLSC',
        'JSBLTFC1',
        'JSTFC11',
        'KELSC4',
        'KFTFC1',
        'MUGHALSC',
        'NEXTCP',
        'P03PFL190623',
        'P03PFL221023',
        'P03PIB050824',
        'P03PIB190922',
        'P03PIB200823',
        'P05GIS091225',
        'P05PFL180625',
        'P05PIB151025',
        'P05PIB190924',
        'P10PFL180630',
        'P10PFL220829',
        'P10PIB101230',
        'P10PIB120728',
        'P10PIB190929',
        'PESC1',
        'PESC2',
        'PK03TB030915',
        'PK03TB090921',
        'PK03TB120821',
        'PK03TB140515',
        'PK03TB211021',
        'PK03TB230921',
        'PK03TB241215',
        'PK03TB260821',
        'PK03TB301221',
        'PK06TB030915',
        'PK06TB070422',
        'PK06TB071021',
        'PK06TB090921',
        'PK06TB100322',
        'PK06TB120821',
        'PK06TB161221',
        'PK06TB181121',
        'PK06TB211021',
        'PK06TB230921',
        'PK06TB241215',
        'PK06TB260821',
        'PK06TB270122',
        'PK06TB301221',
        'PK12TB030915',
        'PK12TB080922',
        'PK12TB100222',
        'PK12TB100322',
        'PK12TB160622',
        'PK12TB190522',
        'PK12TB241215',
        'PK12TB280122',
        'PK12TB301221',
        'SBLTFC',
        'SMBLTFC',
        'SNBLTFC2',
        'SNBLTFC3',
        'SPLCTFC3',
        'UBLTFC5',
        'WTLTFC3',
        'PK03TB021221',
        'PK06TB160217',
        'TFCTRIBL',
        'PACETFC',
        'PK03TB100518',
        'PK12TB100518',
        'PK06TB091117',
        'PK03TB020317',
        'PK12TB140416',
        'TELETFC',
        'PK12TB101116',
        'AZLCLTFC2',
        'PK06TB200815',
        'PK03TB221216',
        'PK03TB060815',
        'PK12TB300415',
        'PK03TB271114',
        'PK03TB251018',
        'PK03TB260516',
        'PK03TB030316',
        'PK06TB231117',
        'PK12TB121017',
        'PK03TB160217',
        'PK12TB231117',
        'PK06TB021221',
        'PK06TB160415',
        'PK12TB221216',
        'PK06TB020317',
        'PK06TB101116',
        'PK03TB140416',
        'PK03TB231117',
        'PK06TB100518',
        'PK03TB060717',
        'PK03TB121017',
        'PK06TB180118',
        'PK12TB140515',
        'PK06TB271114',
        'PK06TB110615',
        'PK03TB111214',
        'PK03TB210116',
        'PK03TB261214',
        'PK06TB140416',
        'NSB10Y1',
        'PK03TB110615',
        'PK12TB180118',
        'PK03TB091117',
        'PK03TB101116',
        'PK12TB080115',
        'PK03TB190215',
        'PK03TB211119',
        'PK06TB030316',
        'PK03TB131114',
        'PK12TB200815',
        'PK06TB251018',
        'PK03TB270918',
        'PK06TB131114',
        'PK03TB300415',
        'PK06TB060815',
        'PK03TB160415',
        'PK12TB210116',
        'PK06TB021014',
        'PK03TB200815',
        'PK12TB260516',
        'PK12TB060215',
        'PK06TB111214',
        'PK12TB110615',
        'PK03TB161014',
        'PK06TB161014',
        'PK12TB160415',
        'PK03TB060215',
        'PK06TB140515',
        'PK06TB060717',
        'PK03TB021014',
        'PK06TB080115',
        'PK06TB300415',
        'PK06TB210116',
        'PK03TB250419',
        'PK03TB180118',
        'PK12TB260821',
        'PK12TB090921',
        'PK12TB230921',
        'PK12TB071021',
        '786',
        'AABS',
        'AAL',
        'AASM',
        'AATM',
        'ABL',
        'ABOT',
        'ABSON',
        'ACPL',
        'ADAMS',
        'ADMM',
        'ADOS',
        'ADTM',
        'AEL',
        'AGHA',
        'AGIC',
        'AGIL',
        'AGL',
        'AGP',
        'AGSML',
        'AGTL',
        'AHCL',
        'AHL',
        'AHTM',
        'AICL',
        'AIRLINK',
        'AKBL',
        'AKDCL',
        'AKDHL',
        'AKGL',
        'AKZO',
        'ALAC',
        'ALNRS',
        'ALQT',
        'ALTN',
        'AMBL',
        'AMSL',
        'AMTEX',
        'ANL',
        'ANNT',
        'ANSM',
        'ANTM',
        'APL',
        'APOT',
        'AQTM',
        'ARM',
        'ARPAK',
        'ARPL',
        'ARUJ',
        'ASC',
        'ASCR1',
        'ASHT',
        'ASIC',
        'ASL',
        'ASRL',
        'ASTL',
        'ASTM',
        'ATBA',
        'ATIL',
        'ATLH',
        'ATRL',
        'AVN',
        'AWTX',
        'AWWAL',
        'AYTM',
        'AYZT',
        'AZMT',
        'AZTM',
        'BAFL',
        'BAFS',
        'BAHL',
        'BAPL',
        'BATA',
        'BCL',
        'BCML',
        'BECO',
        'BEEM',
        'BELA',
        'BERG',
        'BFMOD',
        'BGL',
        'BHAT',
        'BIFO',
        'BIIC',
        'BILF',
        'BIPL',
        'BIPLS',
        'BNL',
        'BNWM',
        'BOK',
        'BOP',
        'BPBL',
        'BPL',
        'BROT',
        'BRR',
        'BTL',
        'BUXL',
        'BWCL',
        'BWHL',
        'BYCO',
        'CASH',
        'CCM',
        'CECL',
        'CENI',
        'CEPB',
        'CFL',
        'CHAS',
        'CHBL',
        'CHCC',
        'CJPL',
        'CLCPS',
        'CLOV',
        'CLVL',
        'COLG',
        'COST',
        'COTT',
        'CPAL',
        'CPHL',
        'CPPL',
        'CRTM',
        'CSAP',
        'CSIL',
        'CSM',
        'CTM',
        'CWSM',
        'CYAN',
        'DAAG',
        'DADX',
        'DATM',
        'DAWH',
        'DBCI',
        'DBSL',
        'DCL',
        'DCM',
        'DCR',
        'DCTL',
        'DEL',
        'DFML',
        'DFSM',
        'DGKC',
        'DIIL',
        'DINT',
        'DKL',
        'DKTM',
        'DLL',
        'DMIL',
        'DMTM',
        'DMTX',
        'DNCC',
        'DOL',
        'DOLCPS',
        'DOMF',
        'DSFL',
        'DSIL',
        'DSL',
        'DSML',
        'DWAE',
        'DWSM',
        'DWTM',
        'DYNO',
        'ECOP',
        'EFERT',
        'EFGH',
        'EFOODS',
        'EFUG',
        'EFUL',
        'ELCM',
        'ELSM',
        'EMCO',
        'ENGL',
        'ENGRO',
        'EPCL',
        'EPCLR1',
        'EPQL',
        'ESBL',
        'EWIC',
        'EWICR1',
        'EWLA',
        'EXIDE',
        'EXTR',
        'FABL',
        'FAEL',
        'FANM',
        'FASM',
        'FATIMA',
        'FCCL',
        'FCEL',
        'FCEPL',
        'FCIBL',
        'FCONM',
        'FCSC',
        'FDIBL',
        'FDMF',
        'FECM',
        'FECTC',
        'FEM',
        'FEROZ',
        'FFBL',
        'FFC',
        'FFL',
        'FFLM',
        'FFLNV',
        'FHAM',
        'FIBLM',
        'FIL',
        'FIM',
        'FIMM',
        'FLYNG',
        'FML',
        'FNBM',
        'FNEL',
        'FPJM',
        'FPRM',
        'FRCL',
        'FRSM',
        'FSWL',
        'FTHM',
        'FTMM',
        'FTSM',
        'FUDLM',
        'FZCM',
        'GADT',
        'GAIL',
        'GAILR1',
        'GAMON',
        'GASF',
        'GATI',
        'GATM',
        'GEMPAPL',
        'GENP',
        'GFIL',
        'GGGL',
        'GGGLR1',
        'GGL',
        'GGLR1',
        'GHGL',
        'GHGLR1',
        'GHNI',
        'GHNL',
        'GIL',
        'GLAT',
        'GLAXO',
        'GLOT',
        'GLPL',
        'GOC',
        'GOEM',
        'GRYL',
        'GSKCH',
        'GSPM',
        'GTECH',
        'GTYR',
        'GUSM',
        'GUTM',
        'GVGL',
        'GWLC',
        'HABSM',
        'HACC',
        'HADC',
        'HAEL',
        'HAFL',
        'HAJT',
        'HAL',
        'HASCOL',
        'HASCOLR1',
        'HATM',
        'HBL',
        'HCAR',
        'HCL',
        'HGFA',
        'HICL',
        'HIFA',
        'HINO',
        'HINOON',
        'HIRAT',
        'HKKT',
        'HMB',
        'HMICL',
        'HMIM',
        'HMM',
        'HRPL',
        'HSM',
        'HSMR1',
        'HSPI',
        'HTL',
        'HUBC',
        'HUMNL',
        'HUSI',
        'HWQS',
        'IBFL',
        'IBLHL',
        'ICCI',
        'ICCT',
        'ICI',
        'ICIBL',
        'ICL',
        'ICLR1',
        'IDRT',
        'IDSM',
        'IDYM',
        'IFSL',
        'IGIBL',
        'IGIHL',
        'IGIIL',
        'IGIL',
        'ILP',
        'ILTM',
        'IMAGE',
        'IMAGER1',
        'IML',
        'IMSL',
        'INDU',
        'INIL',
        'INKL',
        'INL',
        'INMF',
        'ISHT',
        'ISIL',
        'ISL',
        'ISTM',
        'ITSL',
        'ITTEFAQ',
        'JATM',
        'JDMT',
        'JDWS',
        'JGICL',
        'JKSM',
        'JLICL',
        'JOPP',
        'JOVC',
        'JPGL',
        'JSBL',
        'JSCL',
        'JSCLR1',
        'JSGCL',
        'JSIL',
        'JSML',
        'JUBS',
        'JVDC',
        'JVDCR1',
        'KACM',
        'KAKL',
        'KAPCO',
        'KASBM',
        'KCL',
        'KEL',
        'KHSM',
        'KHTC',
        'KHYT',
        'KML',
        'KOHC',
        'KOHE',
        'KOHP',
        'KOHTM',
        'KOIL',
        'KOSM',
        'KPUS',
        'KSBP',
        'KSTM',
        'KTML',
        'LEUL',
        'LINDE',
        'LMSM',
        'LOADS',
        'LOTCHEM',
        'LPCL',
        'LPGL',
        'LPL',
        'LUCK',
        'MACFL',
        'MACTER',
        'MARI',
        'MCB',
        'MCBAH',
        'MDTL',
        'MDTM',
        'MEBL',
        'MEHT',
        'MERIT',
        'MERITR1',
        'MFFL',
        'MFL',
        'MFTM',
        'MIRKS',
        'MLCF',
        'MLCFR1',
        'MODAM',
        'MOHE',
        'MOIL',
        'MOON',
        'MQTM',
        'MRNS',
        'MSCL',
        'MSOT',
        'MTIL',
        'MTL',
        'MUBT',
        'MUGHAL',
        'MUGHALR1',
        'MUKT',
        'MUREB',
        'MWMP',
        'MZSM',
        'NAFL',
        'NAGC',
        'NATF',
        'NATM',
        'NBP',
        'NCL',
        'NCML',
        'NCPL',
        'NESTLE',
        'NETSOL',
        'NEXT',
        'NIB',
        'NICL',
        'NINA',
        'NMFL',
        'NML',
        'NONS',
        'NORS',
        'NPL',
        'NPSM',
        'NRL',
        'NRSL',
        'NSRM',
        'OCTOPUS',
        'OGDC',
        'OLPL',
        'OLSM',
        'OML',
        'ORIXM',
        'ORM',
        'OTSU',
        'PABC',
        'PACE',
        'PAEL',
        'PAKCEM',
        'PAKD',
        'PAKL',
        'PAKMI',
        'PAKOXY',
        'PAKRI',
        'PAKT',
        'PASL',
        'PASM',
        'PCAL',
        'PCML',
        'PDGH',
        'PECO',
        'PGCL',
        'PGF',
        'PGIC',
        'PGLC',
        'PHDL',
        'PIAA',
        'PIAB',
        'PIBTL',
        'PICL',
        'PICT',
        'PIF',
        'PIL',
        'PIM',
        'PINL',
        'PIOC',
        'PKGI',
        'PKGP',
        'PKGS',
        'PMI',
        'PMPK',
        'PMRS',
        'PNGRS',
        'PNSC',
        'POL',
        'POML',
        'POWER',
        'POWERR1',
        'PPL',
        'PPP',
        'PPVC',
        'PREMA',
        'PRET',
        'PRIB',
        'PRIC',
        'PRL',
        'PRLR1',
        'PRWM',
        'PSEL',
        'PSMC',
        'PSO',
        'PSX',
        'PSYL',
        'PTC',
        'PTL',
        'PUDF',
        'QUET',
        'QUICE',
        'QUSW',
        'RAVT',
        'RCML',
        'REDCO',
        'REGAL',
        'REWM',
        'RICL',
        'RMPL',
        'RPL',
        'RUBY',
        'RUPL',
        'SAIF',
        'SALT',
        'SANE',
        'SANSM',
        'SAPL',
        'SAPT',
        'SARC',
        'SASML',
        'SAZEW',
        'SBL',
        'SCBPL',
        'SCHT',
        'SCL',
        'SDIL',
        'SDOT',
        'SEARL',
        'SEARLR1',
        'SEL',
        'SEPCO',
        'SEPL',
        'SERF',
        'SERT',
        'SFAT',
        'SFL',
        'SFLL',
        'SGABL',
        'SGF',
        'SGFL',
        'SGPL',
        'SHCI',
        'SHCM',
        'SHDT',
        'SHEL',
        'SHEZ',
        'SHFA',
        'SHJS',
        'SHNI',
        'SHSML',
        'SIBL',
        'SICL',
        'SIEM',
        'SILK',
        'SINDM',
        'SING',
        'SITC',
        'SJTM',
        'SKRS',
        'SLCL',
        'SLL',
        'SLSO',
        'SLSOPP',
        'SLSOPVI',
        'SLYT',
        'SMBL',
        'SMBLCPSA',
        'SMBLCPSB',
        'SMCPL',
        'SML',
        'SMLR1',
        'SMTM',
        'SNAI',
        'SNBL',
        'SNGP',
        'SPEL',
        'SPL',
        'SPLC',
        'SPLCTFC3',
        'SPWL',
        'SRSM',
        'SRVI',
        'SSGC',
        'SSIC',
        'SSML',
        'SSOM',
        'STCL',
        'STJT',
        'STML',
        'STPL',
        'SUCM',
        'SUHJ',
        'SURAJ',
        'SURC',
        'SUTM',
        'SYS',
        'SZTM',
        'TAJT',
        'TATM',
        'TCLTC',
        'TDIL',
        'TELE',
        'TGL',
        'THALL',
        'THAS',
        'THCCL',
        'TICL',
        'TOMCL',
        'TOWL',
        'TPL',
        'TPLI',
        'TPLP',
        'TPLT',
        'TREET',
        'TREI',
        'TRG',
        'TRIBL',
        'TRIPF',
        'TRPOL',
        'TRSM',
        'TSBL',
        'TSMF',
        'TSML',
        'TSPL',
        'UBDL',
        'UBL',
        'UCAPM',
        'UDPL',
        'UNIC',
        'UNITY',
        'UNITYR1',
        'UPFL',
        'USMT',
        'UVIC',
        'WAHN',
        'WAVES',
        'WAVESR1',
        'WTL',
        'WYETH',
        'YOUW',
        'ZAHID',
        'ZELP',
        'ZHCM',
        'ZIL',
        'ZTL',
        'UBLPETF',
        'NITGETF',
        'MZNPETF',
        'NBPGETF', 
        ), 463,        #463 is the index number of ILP in stocks/tickers dataframe; it will be selected by default
        )
   
    
st.write('Your Selected Stocks Option:', option)

##

with st.spinner('Plotting timeseries data...'):
   time.sleep(5)

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

##
##

data = stocks(option, start=datetime.date(2019, 1, 1), end=datetime.date.today())
#data  #to see data table delete # at extreme left
data1 = data.reset_index(inplace=True) #to put dates in first colums of dataframe




# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    fig.update_layout(
    autosize=True, height=600, width=700,
    margin=dict(t=60, b=0, l=40, r=40),
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="",
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=20, family="roboto, sans-serif"),    #font of lablels of axises
    bargap=0.2,                             #value can be An int or float in the interval [0, 1]
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
 )
    st.plotly_chart(fig)


plot_raw_data()




# Predict forecast with Prophet.
df_train = data[['Date', 'Close']] #training dataframe
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"}) #rename data colums to 'ds',  and Close column to 'y', so that prophet can read

m = Prophet()   #m is model
m.fit(df_train) #model fit
future = m.make_future_dataframe(periods=period) #future dataframe
forecast = m.predict(future) #prediction in forecast dataframe



##

with st.spinner('Preparing the forecast...'):
   time.sleep(5)

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

##
# Show and plot forecast
st.subheader('Forecast data')
forecast #complete prediction dataframe
#st.write(forecast.tail()) #to see tail of forecast dataframe




##

with st.spinner('Plotting the forecast...'):
   time.sleep(5)

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

##
#st.subheader(f'Forecast plot for {n_years} years')
st.subheader('Forecast plot')

fig1 = plot_plotly(m, forecast)
fig1.update_layout(
    autosize=True, height=600, width=700,
    margin=dict(t=60, b=0, l=40, r=40),
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="",
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=20, family="roboto, sans-serif"),    #font of lablels of axises
    bargap=0.2,                             #value can be An int or float in the interval [0, 1]
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)
st.plotly_chart(fig1)

st.subheader("Forecast components")

fig2 = m.plot_components(forecast)

st.write(fig2)






