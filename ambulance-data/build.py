import re,html,hashlib,os,csv,datetime,subprocess,pdfplumber
R='raw'
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def ft(p): return datetime.datetime.fromtimestamp(os.path.getmtime(p)).strftime('%Y-%m-%d %H:%M (UTC+8)')
def htxt(p):
    t=open(p,errors='ignore').read(); t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); return re.sub(r'\s+',' ',t)
def ptxt(p):
    with pdfplumber.open(p) as d: return re.sub(r'\s+',' ',' '.join((pg.extract_text() or '') for pg in d.pages))
def ocr(p,page):
    import tempfile
    td=tempfile.mkdtemp(); subprocess.run(['pdftoppm','-r','300','-f',str(page),'-l',str(page),'-png',p,os.path.join(td,'o')],check=True)
    f=os.path.join(td,os.listdir(td)[0]); t=subprocess.run(['tesseract',f,'-'],capture_output=True,text=True).stdout; os.remove(f); os.rmdir(td); return re.sub(r'\s+',' ',t)
cache={}
def A(src,regex,mode='auto',page=1):
    k=(src,mode,page)
    if k not in cache:
        p=os.path.join(R,src); cache[k]= htxt(p) if p.endswith('.html') else (ocr(p,page) if mode=='ocr' else ptxt(p))
    m=re.search(regex,cache[k]); 
    return m.group(1).replace(',','') if m else None
U={}
# rows: jur, op, svc, res, manual_amount, unit, ptype, eff, ref, src_file, url, regexA, quote(B), mode, page
rows=[
# New York
('New York, NY','FDNY (New York City Fire Department)','BLS','不分','1793','per transport','实收','2026-07-01','3 RCNY §8400-02','new-york/3rcny-8400-02-adoption.pdf','https://rules.cityofnewyork.us/wp-content/uploads/2026/05/Notice-of-Adoption-of-Amendments-to-Fire-Department-Rule-3-RCNY-8400-02-Schedule-of-Charges-for-Fire-Department-Ambulance-Treatment-and-Transport-Services.pdf',r'Basic Life Support Ambulance \[\$1,385\.00\] \$([\d,]+)','Basic Life Support Ambulance [$1,385.00] $1,793.00'),
('New York, NY','FDNY (New York City Fire Department)','BLS','不分','1385','per transport','实收','2023-05-01（旧版，已被 2026-07-01 取代）','3 RCNY §8400-02','new-york/3rcny-8400-02-adoption.pdf','同上',r'Basic Life Support Ambulance \[\$([\d,]+)\.00\]','[Deleted material] Basic Life Support Ambulance [$1,385.00]'),
('New York, NY','FDNY (New York City Fire Department)','ALS1','不分','2196','per transport','实收','2026-07-01','3 RCNY §8400-02','new-york/3rcny-8400-02-adoption.pdf','同上',r'\[\$1,680\.00\] \$([\d,]+)','Advanced Life Support Ambulance Service Level 1 (ALS1) [$1,680.00] $2,196.00'),
('New York, NY','FDNY (New York City Fire Department)','ALS2','不分','2212','per transport','实收','2026-07-01','3 RCNY §8400-02','new-york/3rcny-8400-02-adoption.pdf','同上',r'\[\$1,692\.00\] \$([\d,]+)','Advanced Life Support Ambulance Service Level 2 (ALS2) [$1,692.00] $2,212.00'),
('New York, NY','FDNY (New York City Fire Department)','non_transport (BLS 现场处置)','不分','896','per patient','实收','2026-07-01','3 RCNY §8400-02','new-york/3rcny-8400-02-adoption.pdf','同上',r'\[\$630\.00\] \$([\d,]+)','Basic Life Support Ambulance Treatment in Place ... [$630.00] $896.00'),
('New York, NY','FDNY (New York City Fire Department)','non_transport (ALS 现场处置)','不分','1098','per patient','实收','2026-07-01','3 RCNY §8400-02','new-york/3rcny-8400-02-adoption.pdf','同上',r'\[\$1,050\.00\] \$([\d,]+)','Advanced Life Support Ambulance Treatment in Place ... [$1,050.00] $1,098.00'),
('New York, NY','FDNY (New York City Fire Department)','mileage','不分','20','per loaded mile','实收','2026-07-01','3 RCNY §8400-02','new-york/3rcny-8400-02-adoption.pdf','同上',r'\$([\d.]+)/mile','Mileage (distance traveled to hospital or medical facility with patient) $20.00/mile'),
('New York, NY','FDNY (New York City Fire Department)','其他(氧气)','不分','66','per item','实收','2026-07-01','3 RCNY §8400-02','new-york/3rcny-8400-02-adoption.pdf','同上',r'Oxygen \(as applicable\) \$([\d.]+)','Provision of Oxygen (as applicable) $66.00'),
# Los Angeles
('Los Angeles, CA','LAFD (Los Angeles Fire Department)','BLS','不分','2068','per patient','实收','2026-09-30','LAAC §22.210.2(b)；Ord. 189020','los-angeles/ord_189020.pdf','https://cityclerk.lacity.org/onlinedocs/2025/25-0410_ord_189020_09-30-26.pdf',r'Basic Life Support Fee, Each Patient \$([\d,]+)','Basic Life Support Fee, Each Patient $2,068.00 … Ordinance Effective Date: 09/30/2026','ocr',1),
('Los Angeles, CA','LAFD (Los Angeles Fire Department)','BLS','不分','1862','per patient','实收','2026-04-30（旧版，2026-09-30 被 Ord.189020 取代）','LAAC §22.210.2(b)；Ord. 188894','los-angeles/ord_188894.pdf','https://cityclerk.lacity.org/onlinedocs/2025/25-0410_ord_188894_4-30-26.pdf',r'Basic Life Support Fee, Each Patient \$([\d,]+)','Basic Life Support Fee, Each Patient $1,862.00','ocr',1),
('Los Angeles, CA','LAFD (Los Angeles Fire Department)','ALS','不分','2915','per patient','实收','2026-04-30','LAAC §22.210.2(b)；Ord. 188894','los-angeles/ord_188894.pdf','https://cityclerk.lacity.org/onlinedocs/2025/25-0410_ord_188894_4-30-26.pdf',r'Advanced Life Support Fee, Each Patient \$([\d,]+)','Advanced Life Support Fee, Each Patient $2,915.00','ocr',1),
('Los Angeles, CA','LAFD (Los Angeles Fire Department)','mileage','不分','29','per mile (one way)','实收','2026-04-30','LAAC §22.210.2(b)；Ord. 188894','los-angeles/ord_188894.pdf','https://cityclerk.lacity.org/onlinedocs/2025/25-0410_ord_188894_4-30-26.pdf',r'Per Mile \$ ?([\d,]+)','Mileage One Way - Per Mile $ 29.00','ocr',1),
# Chicago
('Chicago, IL','Chicago Fire Department（由财政局收费）','BLS','不分','3234','per transport','实收','2026-01-03','MCC §4-68-130、§2-32-096；Department of Finance Ambulance Rules（2025-12-22 签署，2025-12-24 发布）','chicago/Ambulance_Rules_2026_browser.pdf','https://www.chicago.gov/content/dam/city/depts/dol/rulesandregs/Ambulance_Rules_2026.pdf',r'Basic Life Support: \$([\d,]+)','Basic Life Support: $3,234'),
('Chicago, IL','Chicago Fire Department（由财政局收费）','ALS','不分','3384','per transport','实收','2026-01-03','MCC §4-68-130、§2-32-096；Department of Finance Ambulance Rules（2025-12-22 签署，2025-12-24 发布）','chicago/Ambulance_Rules_2026_browser.pdf','https://www.chicago.gov/content/dam/city/depts/dol/rulesandregs/Ambulance_Rules_2026.pdf',r'Advanced Life Support: \$([\d,]+)','Advanced Life Support: $3,384'),
('Chicago, IL','Chicago Fire Department（由财政局收费）','mileage','不分','19','per mile','实收','2026-01-03','MCC §4-68-130、§2-32-096；Department of Finance Ambulance Rules（2025-12-22 签署，2025-12-24 发布）','chicago/Ambulance_Rules_2026_browser.pdf','https://www.chicago.gov/content/dam/city/depts/dol/rulesandregs/Ambulance_Rules_2026.pdf',r'Ambulance transport: \$([\d,]+) per mile','Ambulance transport: $19 per mile'),
('Chicago, IL','Chicago Fire Department（由财政局收费）','其他(氧气)','不分','28','per item','实收','2026-01-03','MCC §4-68-130、§2-32-096；Department of Finance Ambulance Rules（2025-12-22 签署，2025-12-24 发布）','chicago/Ambulance_Rules_2026_browser.pdf','https://www.chicago.gov/content/dam/city/depts/dol/rulesandregs/Ambulance_Rules_2026.pdf',r'Oxygen service: \$([\d,]+)','Oxygen service: $28'),
# Houston
('Houston, TX','Houston Fire Department（市财政局开单）','BLS/ALS 不分(治疗+转运)','不分','2158.16','per transport','实收','2026-01-01','Houston Code §4-13(a)(1)','houston/fee-schedule.html','https://cohweb.houstontx.gov/FIN_FeeSchedule/',r'Treatment and Transport 4-13\(a\)\(1\) \$([\d,.]+)','EMS/Ambulance Service Treatment and Transport 4-13(a)(1) $2,158.16 01/01/2026'),
('Houston, TX','Houston Fire Department（市财政局开单）','mileage','不分','16.52','per mile or portion','实收','2026-01-01','Houston Code §4-13(a)(2)','houston/fee-schedule.html','同上',r'portion of a mile 4-13\(a\)\(2\) \$([\d,.]+)','Mileage, per mile or any portion of a mile 4-13(a)(2) $16.52 01/01/2026'),
('Houston, TX','Houston Fire Department（市财政局开单）','non_transport','不分','201.28','per patient','实收','2026-01-01','Houston Code §4-13(a)(4)','houston/fee-schedule.html','同上',r'Treatment without transport 4-13\(a\)\(4\) \$([\d,.]+)','Treatment without transport 4-13(a)(4) $201.28 01/01/2026'),
('Houston, TX','Houston Fire Department（市财政局开单）','其他(现场终止抢救)','不分','419.81','per response','实收','2026-01-01','Houston Code §4-13(a)(3)','houston/fee-schedule.html','同上',r'Field termination response 4-13\(a\)\(3\) \$([\d,.]+)','Field termination response 4-13(a)(3) $419.81 01/01/2026'),
('Houston, TX','Houston Fire Department（市财政局开单）','其他(扶起服务，第4次起)','不分','201.28','per response','实收','2026-01-01','Houston Code §4-13(a)(5)','houston/fee-schedule.html','同上',r'Lift response 4-13\(a\)\(5\) \$([\d,.]+)','Lift response 4-13(a)(5) $201.28 01/01/2026'),
# Phoenix
('Phoenix, AZ','Phoenix ETS (Emergency Transportation Services), City of Phoenix','ALS','不分','1224.39','per transport','上限','2026-04-17','AZDHS 地面救护车费率表（A.R.S. §36-2232/2239 核准的一般公众费率），CON No. 76','phoenix/azdhs-ground-ambulance-rate-schedule.pdf','https://www.azdhs.gov/documents/preparedness/emergency-medical-services-trauma-system/ambulance/ground/rates/ground-ambulance-rate-schedule.pdf',r'City of \*\*\* \( ?([\d,.]+)\)','Phoenix ETS (Emergency Transportation Services), 76 muni City of *** ( 1,224.39) ( 1,090.65) ( 25.39) ( 272.66) 00117 04/17/26 Yes'),
('Phoenix, AZ','Phoenix ETS (Emergency Transportation Services), City of Phoenix','BLS','不分','1090.65','per transport','上限','2026-04-17','同上','phoenix/azdhs-ground-ambulance-rate-schedule.pdf','同上',r'City of \*\*\* \( ?[\d,.]+\) \( ?([\d,.]+)\)','同上'),
('Phoenix, AZ','Phoenix ETS (Emergency Transportation Services), City of Phoenix','mileage','不分','25.39','per mile','上限','2026-04-17','同上','phoenix/azdhs-ground-ambulance-rate-schedule.pdf','同上',r'City of \*\*\* \( ?[\d,.]+\) \( ?[\d,.]+\) \( ?([\d,.]+)\)','同上'),
('Phoenix, AZ','Phoenix ETS (Emergency Transportation Services), City of Phoenix','其他(待命/等候)','不分','272.66','per hour（单位原件表头未写，按 AZDHS 惯例为每小时，待核）','上限','2026-04-17','同上','phoenix/azdhs-ground-ambulance-rate-schedule.pdf','同上',r'City of \*\*\* \( ?[\d,.]+\) \( ?[\d,.]+\) \( ?[\d,.]+\) \( ?([\d,.]+)\)','同上'),
# San Antonio
('San Antonio, TX','San Antonio Fire Department EMS','BLS','不分','1700','per patient','实收','2026-10-01','City Code（页面未写条号）','san-antonio/ems-billing.html','https://www.sa.gov/Directory/Departments/SAFD/Reports-Billing/EMS-Reports/EMS-Billing',r'basic life support emergency medical services \$([\d,]+)','Patient transport requiring basic life support emergency medical services $1,700 + $12 per mile'),
('San Antonio, TX','San Antonio Fire Department EMS','ALS1','不分','1700','per patient','实收','2026-10-01','City Code（页面未写条号）','san-antonio/ems-billing.html','同上',r'Level I emergency medical services \$([\d,]+)','…advanced life support Level I emergency medical services $1,700 + $12 per mile'),
('San Antonio, TX','San Antonio Fire Department EMS','ALS2','不分','1700','per patient','实收','2026-10-01','City Code（页面未写条号）','san-antonio/ems-billing.html','同上',r'Level II emergency medical services \$([\d,]+)','…advanced life support Level II emergency medical services $1,700 + $12 per mile'),
('San Antonio, TX','San Antonio Fire Department EMS','mileage','不分','12','per mile','实收','2026-10-01','City Code（页面未写条号）','san-antonio/ems-billing.html','同上',r'\+ \$([\d,]+) per mile','$1,700 + $12 per mile'),
('San Antonio, TX','San Antonio Fire Department EMS','其他(非居民附加费)','非居民','100','per patient','实收','2026-10-01','City Code（页面未写条号）','san-antonio/ems-billing.html','同上',r'nonresident patient \$([\d,]+)','Transport fee surcharge for each nonresident patient $100'),
('San Antonio, TX','San Antonio Fire Department EMS','non_transport','不分','150','per call','实收','2026-10-01','City Code（页面未写条号）','san-antonio/ems-billing.html','同上',r'Non-transport emergency medical services call \$([\d,]+)','Non-transport emergency medical services call $150'),
('San Antonio, TX','San Antonio Fire Department EMS','其他(扶起服务 Lift Assist)','不分','1291','未写','实收','2026-10-01','City Code（页面未写条号）','san-antonio/ems-billing.html','同上',r'Lift Assist: \$([\d,]+)','Lift Assist: $1291'),
# Dallas
('Dallas, TX','Dallas Fire-Rescue','BLS/ALS 不分(转运)','居民','1473','per transport','实收','2023-09（旧版，2026-09-16 被 Ord.33564 取代）','Dallas City Code §15D-5(b)(1)；Ord. 32556','dallas/ord-32556.pdf','https://files.amlegal.com/pdffiles/Dallas/32556.pdf',r'\(1\) \$1[.,]?(\d{3})','(1) $1,473[1,368] for each transport of a resident of the city of Dallas to a hospital','ocr',7),
('Dallas, TX','Dallas Fire-Rescue','BLS/ALS 不分(转运)','非居民','1868','per transport','实收','2023-09（旧版，2026-09-16 被 Ord.33564 取代）','同上','dallas/ord-32556.pdf','同上',r'and \$ ?1,?(\d{3}) for each transport of a nonresident','$ 1,868 for each transport of a nonresident of the city of Dallas to a hospital','ocr',7),
('Dallas, TX','Dallas Fire-Rescue','non_transport','不分','125','per patient','实收','2023-09（旧版，2026-09-16 被 Ord.33564 取代）','Dallas City Code §15D-5(b)(2)','dallas/ord-32556.pdf','同上',r'\(2\) \$(\d+) for treatment','(2) $125 for treatment of a person who is not transported by ambulance.','ocr',7),
('Dallas, TX','Dallas Fire-Rescue','mileage','不分','10','per loaded mile','实收','2023-09（旧版，2026-09-16 被 Ord.33564 取代）','Dallas City Code §15D-5(b)(6)','dallas/ord-32556.pdf','同上',r'\(6\) \$(\d+)','(6) $10[+5] for each loaded mile of transport by ambulance','ocr',8),
('Dallas, TX','Dallas Fire-Rescue','BLS/ALS 不分(转运)','居民','1575','per transport','实收','2026-09-16（Ord.33564 通过并即时生效）','Dallas City Code §15D-5(b)(1)；Ord. 33564 Sec.10','dallas/ord-33564.pdf','https://citysecretary2.dallascityhall.com/resolutions/2026/09-16-26/26-1450.pdf',r'\(1\) \$(1[.,]?\d{3})','(1) $1.575 for each transport of a resident of the city of Dallas to a hospital（原件扫描把逗号识成句点，人工确认为 $1,575）'),
('Dallas, TX','Dallas Fire-Rescue','BLS/ALS 不分(转运)','非居民','1868','per transport','实收','2026-09-16（Ord.33564 通过并即时生效）','同上','dallas/ord-33564.pdf','同上',r'hospital and \$ ?(1,?\d{3}) for each transport of a nonresident','hospital and $1,868 for each transport of a nonresident of the city of Dallas to a hospital'),
('Dallas, TX','Dallas Fire-Rescue','non_transport','不分','295','per patient','实收','2026-09-16（Ord.33564 通过并即时生效）','Dallas City Code §15D-5(b)(2)；Ord. 33564','dallas/ord-33564.pdf','同上',r'\(2\) \$(\d+)','(2) $295 for treatment of a person who is not transported by ambulance.'),
('Dallas, TX','Dallas Fire-Rescue','mileage','不分','9','per loaded mile','实收','2026-09-16（Ord.33564 通过并即时生效）','Dallas City Code §15D-5(b)(6)；Ord. 33564','dallas/ord-33564.pdf','同上',r'\(6\) \$(\d+)','(6) $9 for each loaded mile of transport by ambulance'),
# San Diego
('San Diego, CA','San Diego Fire-Rescue（市政收费；联盟模式含 AMR）','ALS2','不分','3371.91','per incident','未明确','2025-07-01（FY2026 表；按 R-316243 另有 FY2027 上调 5% 自 2026-07-01 起，金额未取得，本表可能已过期）','FY2026 User Fee Schedule；Council Resolution R-316243（2025-06-05 终审通过）','san-diego/fy26-user-fee-schedule.pdf','https://www.sandiego.gov/sites/default/files/2025-06/fy26-user-fee-schedule.pdf',r'ALS Emergency Transport Level 2 \$([\d,.]+)','ALS Emergency Transport Level 2 $3,371.91 per incident'),
('San Diego, CA','San Diego Fire-Rescue（市政收费；联盟模式含 AMR）','ALS1','不分','3228.92','per incident','未明确','2025-07-01（FY2026 表；按 R-316243 另有 FY2027 上调 5% 自 2026-07-01 起，金额未取得，本表可能已过期）','FY2026 User Fee Schedule；Council Resolution R-316243（2025-06-05 终审通过）','san-diego/fy26-user-fee-schedule.pdf','https://www.sandiego.gov/sites/default/files/2025-06/fy26-user-fee-schedule.pdf',r'ALS Emergency Transport Level 1 \$([\d,.]+)','ALS Emergency Transport Level 1 $3,228.92 per incident'),
('San Diego, CA','San Diego Fire-Rescue（市政收费；联盟模式含 AMR）','BLS','不分','2724.33','per incident','未明确','2025-07-01（FY2026 表；按 R-316243 另有 FY2027 上调 5% 自 2026-07-01 起，金额未取得，本表可能已过期）','FY2026 User Fee Schedule；Council Resolution R-316243（2025-06-05 终审通过）','san-diego/fy26-user-fee-schedule.pdf','https://www.sandiego.gov/sites/default/files/2025-06/fy26-user-fee-schedule.pdf',r'BLS Emergency Transport \$([\d,.]+)','BLS Emergency Transport $2,724.33 per incident'),
('San Diego, CA','San Diego Fire-Rescue（市政收费；联盟模式含 AMR）','non_transport','不分','255.91','per incident','未明确','2025-07-01（FY2026 表；按 R-316243 另有 FY2027 上调 5% 自 2026-07-01 起，金额未取得，本表可能已过期）','FY2026 User Fee Schedule；Council Resolution R-316243（2025-06-05 终审通过）','san-diego/fy26-user-fee-schedule.pdf','https://www.sandiego.gov/sites/default/files/2025-06/fy26-user-fee-schedule.pdf',r'Treat, No Transport \$([\d,.]+)','ALS or BLS Treat, No Transport $255.91 per incident'),
('San Diego, CA','San Diego Fire-Rescue（市政收费；联盟模式含 AMR）','mileage','不分','49.13','per incident','未明确','2025-07-01（FY2026 表；按 R-316243 另有 FY2027 上调 5% 自 2026-07-01 起，金额未取得，本表可能已过期）','FY2026 User Fee Schedule；Council Resolution R-316243（2025-06-05 终审通过）','san-diego/fy26-user-fee-schedule.pdf','https://www.sandiego.gov/sites/default/files/2025-06/fy26-user-fee-schedule.pdf',r'Mileage \$([\d,.]+)','Mileage $49.13 per incident'),
# Las Vegas
('Las Vegas, NV','多家非排他特许经营商（AMR、MedicWest 等，价格上限文件不分商家）','ALS1','不分','1355.91','per transport','上限','2026-02-01','LVMC 6.08.190','las-vegas/2026_max_rates.pdf','https://files.lasvegasnevada.gov/finance/Franchise/2026_Maximum_Allowable_Ambulance_Service_Rates-Effective-Feb-1-2026.pdf',r'Emergency response ALS 1 \$([\d,.]+)','Emergency response ALS 1 $1,355.91'),
('Las Vegas, NV','同上','ALS2','不分','1484.39','per transport','上限','2026-02-01','LVMC 6.08.190','las-vegas/2026_max_rates.pdf','同上',r'Emergency response ALS 2 \$([\d,.]+)','Emergency response ALS 2 $1,484.39'),
('Las Vegas, NV','同上','BLS','不分','1288.63','per transport','上限','2026-02-01','LVMC 6.08.190','las-vegas/2026_max_rates.pdf','同上',r'Emergency response BLS \$([\d,.]+)','Emergency response BLS $1,288.63'),
('Las Vegas, NV','同上','其他(非急诊 ALS)','不分','1209.06','per transport','上限','2026-02-01','LVMC 6.08.190','las-vegas/2026_max_rates.pdf','同上',r'Non-emergency response ALS \$([\d,.]+)','Non-emergency response ALS $1,209.06'),
('Las Vegas, NV','同上','其他(非急诊 BLS)','不分','1154.08','per transport','上限','2026-02-01','LVMC 6.08.190','las-vegas/2026_max_rates.pdf','同上',r'Non-emergency response BLS \$([\d,.]+)','Non-emergency response BLS $1,154.08'),
('Las Vegas, NV','同上','其他(重症转运 CCT)','不分','1610.79','per transport','上限','2026-02-01','LVMC 6.08.190','las-vegas/2026_max_rates.pdf','同上',r'Critical care transport \$([\d,.]+)','Critical care transport $1,610.79'),
('Las Vegas, NV','同上','mileage','不分','38.35','per loaded mile','上限','2026-02-01','LVMC 6.08.190','las-vegas/2026_max_rates.pdf','同上',r'Loaded mileage charge \$([\d,.]+)','Loaded mileage charge $38.35'),
# DC
('Washington, DC','DC Fire and EMS Department (FEMS)','BLS/ALS 不分(转运)','不分','2000','per transport','上限','2026-01-01','D.C. Code §5-416','washington-dc/dc-code-5-416.html','https://code.dccouncil.gov/us/dc/council/code/sections/5-416',r'\$([\d,]+), beginning January 1, 2026; and \(2\)','no more than: … (F) $2,000, beginning January 1, 2026'),
('Washington, DC','DC Fire and EMS Department (FEMS)','BLS/ALS 不分(转运)','不分','1750','per transport','上限','2025-01-01（旧版）','D.C. Code §5-416','washington-dc/dc-code-5-416.html','同上',r'\$([\d,]+), beginning January 1, 2025; and \(F\) \$2,000','(E) $1,750, beginning January 1, 2025'),
('Washington, DC','DC Fire and EMS Department (FEMS)','mileage','不分','30','per mile or fraction','上限','2026-01-01','D.C. Code §5-416','washington-dc/dc-code-5-416.html','同上',r'\(F\) \$([\d.]+), beginning January 1, 202','(F) $30, beginning January 1, 2026'),
('Washington, DC','DC Fire and EMS Department (FEMS)','mileage','不分','26.25','per mile or fraction','上限','2025-01-01（旧版）','D.C. Code §5-416','washington-dc/dc-code-5-416.html','同上',r'\(E\) \$([\d.]+), beginning January 1, 2025; and \(F\) \$30','(E) $26.25, beginning January 1, 2025'),
]
NPI={ # 来源：NPPES 公开 API（2026-10-29 查询）；只收名称+城市+州+救护车分类均对上的
'New York, NY':('未取得（候选：1083715460，法人为 NYC Health and Hospitals Corp，DBA "NYC FIRE DEPT-EMS AMBULANCE"，法人名与 FDNY 不一致）','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1083715460'),
'Los Angeles, CA':('1083789564','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1083789564'),
'Chicago, IL':('1376554592','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1376554592'),
'Houston, TX':('1447375282','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1447375282'),
'Phoenix, AZ':('未取得（候选：1982781571 CITY OF PHOENIX ARIZONA / DBA CITY OF PHOENIX ETS，主分类为 Paramedic 而非 Ambulance）','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1982781571'),
'San Antonio, TX':('1053377713','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1053377713'),
'Dallas, TX':('1861530990','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1861530990'),
'San Diego, CA':('1043904485','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1043904485'),
'Las Vegas, NV':('多候选（AMR=Mercy Inc 1235232562；MedicWest Ambulance Inc 有 1962439026/1265065130/1003006180 三个）','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1235232562'),
'Washington, DC':('1992805022','https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1992805022'),
}
out=[];stats={}
for r in rows:
    jur,op,svc,res,amt,unit,pt,eff,ref,src,url,rx,quote=r[:13]; mode=r[13] if len(r)>13 else 'auto'; page=r[14] if len(r)>14 else 1
    a=A(src,rx,mode,page)
    if a is not None and mode=='ocr' and src.startswith('dallas') and len(a)==3 and ('1,'+a) : a='1'+a if svc.startswith('BLS') else a
    aval=None if a is None else float(a)
    if aval is not None and abs(aval-float(amt))<0.005: cs='两路一致'
    else: cs='不一致待看'
    if a=='1.575': cs='人工确认'
    if url=='同上': url=prev_url
    prev_url=url
    p=os.path.join(R,src)
    out.append(dict(jurisdiction=jur,operator=op,npi=NPI[jur][0],npi_source=NPI[jur][1],service_type=svc,resident_type=res,amount=amt,unit=unit,price_type=pt,effective_date=eff,ordinance_ref=ref,source_url=url,fetched_at=ft(p),sha256=sha(p),evidence_tier='官方原件',check_status=cs,path_a_method=('OCR(tesseract)' if mode=='ocr' else ('HTML解析' if src.endswith('html') else 'pdfplumber')),path_a_value=a or '未抽到',path_b_quote=quote,raw_file=src))
    stats.setdefault(jur,[0,0]); stats[jur][0]+=1; stats[jur][1]+= cs!='两路一致'
with open('rates.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for k,v in stats.items(): print(k,v)
with open('sources.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['file','sha256','fetched_at','bytes'])
    for d,_,fs in os.walk(R):
        for x in sorted(fs): p=os.path.join(d,x); w.writerow([p[4:],sha(p),ft(p),os.path.getsize(p)])
