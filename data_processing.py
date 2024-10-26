import csv
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据 train/test
file = "test.csv"
data = pd.read_csv(file, low_memory = False)
customer = pd.DataFrame(data)

# 异常值,缺失值 检测
## age
age = pd.DataFrame(customer["age"])
age.plot.box()
age_NAN=age.isnull().sum()
print("age NAN:",age_NAN)
plt.savefig("./process_pic_test/age.png")


## job
job=pd.DataFrame(customer["job"])
job_NAN=job.isnull().sum()
job_count=job.value_counts()
print("job NAN:",job_NAN)
print("job count:",job_count)

## marital
marital=pd.DataFrame(customer["marital"])
marital_NAN=marital.isnull().sum()
marital_count=marital.value_counts()
print("marital NAN:",marital_NAN)
print("marital count:",marital_count)

## education
education=pd.DataFrame(customer["education"])
education_NAN=education.isnull().sum()
education_count=education.value_counts()
print("education NAN:",education_NAN)
print("education count:",education_count)

## default
default=pd.DataFrame(customer["default"])
default_NAN=default.isnull().sum()
default_count=default.value_counts()
print("default NAN:",default_NAN)
print("default count:",default_count)

## housing
housing=pd.DataFrame(customer["housing"])
housing_NAN=housing.isnull().sum()
housing_count=housing.value_counts()
print("housing NAN:",housing_NAN)
print("housing count:",housing_count)

## loan
loan=pd.DataFrame(customer["loan"])
loan_NAN=loan.isnull().sum()
loan_count=loan.value_counts()
print("loan NAN:",loan_NAN)
print("loan count:",loan_count)

## contact
contact=pd.DataFrame(customer["contact"])
contact_NAN=contact.isnull().sum()
contact_count=contact.value_counts()
print("contact NAN:",contact_NAN)
print("contact count:",contact_count)

## month
month=pd.DataFrame(customer["month"])
month_NAN=month.isnull().sum()
month_count=month.value_counts()
print("month NAN:",month_NAN)
print("month count:",month_count)

## week
week=pd.DataFrame(customer["day_of_week"])
week_NAN=week.isnull().sum()
week_count=week.value_counts()
print("week NAN:",week_NAN)
print("week count:",week_count)

## duration
duration = pd.DataFrame(customer["duration"])
duration.plot.box()
duration_NAN=duration.isnull().sum()
print("duration NAN:",duration_NAN)
plt.savefig("./process_pic_test/duration.png")

## campaign
campaign = pd.DataFrame(customer["campaign"])
campaign.plot.box()
campaign_NAN=campaign.isnull().sum()
print("campaign NAN",campaign_NAN)
plt.savefig("./process_pic_test/campaign.png")

## pdays
pdays = pd.DataFrame(customer["pdays"])
pdays.plot.box()
pdays_NAN=pdays.isnull().sum()
print("pdays NAN",pdays_NAN)
plt.savefig("./process_pic_test/pdays.png")

## previous
previous = pd.DataFrame(customer["previous"])
previous.plot.box()
previous_NAN=previous.isnull().sum()
print("previous NAN",previous_NAN)
plt.savefig("./process_pic_test/previous.png")

## poutcome
poutcome=pd.DataFrame(customer["poutcome"])
poutcome_NAN=poutcome.isnull().sum()
poutcome_count=poutcome.value_counts()
print("poutcome NAN:",poutcome_NAN)
print("poutcome count:",poutcome_count)

## emp_var_rate
emp = pd.DataFrame(customer["emp_var_rate"])
emp.plot.box()
emp_NAN=emp.isnull().sum()
print("emp_var_rate NAN",emp_NAN)
plt.savefig("./process_pic_test/emp_var_rate.png")

## cons_price_index
cons_price = pd.DataFrame(customer["cons_price_index"])
cons_price.plot.box()
cons_price_NAN=cons_price.isnull().sum()
print("cons_price_index NAN",cons_price_NAN)
plt.savefig("./process_pic_test/cons_price_index.png")

## cons_conf_index
cons_conf_index = pd.DataFrame(customer["cons_conf_index"])
cons_conf_index.plot.box()
cons_conf_index_NAN=cons_conf_index.isnull().sum()
print("cons_conf_index NAN",cons_conf_index_NAN)
plt.savefig("./process_pic_test/cons_conf_index.png")

## lending_rate3m
lending_rate3m = pd.DataFrame(customer["lending_rate3m"])
lending_rate3m.plot.box()
lending_rate3m_NAN=lending_rate3m.isnull().sum()
print("lending_rate3m NAN",lending_rate3m_NAN)
plt.savefig("./process_pic_test/lending_rate3m.png")

## nr_employed
nr_employed = pd.DataFrame(customer["nr_employed"])
nr_employed.plot.box()
nr_employed_NAN=nr_employed.isnull().sum()
print("nr_employed NAN",nr_employed_NAN)
plt.savefig("./process_pic_test/nr_employed.png")

## subscribe
# subscribe=pd.DataFrame(customer["subscribe"])
# subscribe_NAN=subscribe.isnull().sum()
# subscribe_count=subscribe.value_counts()
# print("subscribe NAN:",subscribe_NAN)
# print("subscribe count:",subscribe_count)


plt.show()



