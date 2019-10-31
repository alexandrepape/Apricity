from src import db


class Census_learn_sql(db.Model):
    __tablename__ = 'census_learn_sql'
    age = db.Column(db.Integer, primary_key=True)
    class_of_worker = db.Column("class of worker", db.VARCHAR(1000))
    industry_code = db.Column("industry code", db.VARCHAR(1000))
    occupation_code = db.Column("occupation code", db.VARCHAR(1000))
    education = db.Column(db.VARCHAR(1000))
    wage_per_hour = db.Column("wage per hour", db.VARCHAR(1000))
    last_education = db.Column("last education", db.VARCHAR(1000))
    marital_status = db.Column("marital status", db.VARCHAR(1000))
    major_industry_code = db.Column("major industry code", db.VARCHAR(1000))
    major_occupation_code = db.Column("major occupation code", db.VARCHAR(1000))
    mace = db.Column(db.VARCHAR(1000))
    hispanice = db.Column(db.VARCHAR(1000))
    sex = db.Column(db.VARCHAR(1000))
    member_of_labor = db.Column("member of labor", db.VARCHAR(1000))
    reason_for_unemployment = db.Column("reason for unemployment", db.VARCHAR(1000))
    fulltime = db.Column(db.VARCHAR(1000))
    capital_gain = db.Column("capital gain", db.VARCHAR(1000))
    capital_loss = db.Column("capital loss", db.VARCHAR(1000))
    dividends = db.Column(db.VARCHAR(1000))
    income_tax_liability = db.Column("income tax liability", db.VARCHAR(1000))
    previous_residence_region = db.Column("previus residence region", db.VARCHAR(1000))
    previous_residence_state = db.Column("previus residence state", db.VARCHAR(1000))
    household_with_family = db.Column("household-with-family", db.VARCHAR(1000))
    household_simple = db.Column("household-simple", db.VARCHAR(1000))
    weight = db.Column(db.VARCHAR(1000))
    msa_change = db.Column("msa-change", db.VARCHAR(1000))
    reg_change = db.Column("reg-change", db.VARCHAR(1000))
    within_reg_change = db.Column("within-reg-change", db.VARCHAR(1000))
    lived_here = db.Column("lived-here", db.VARCHAR(1000))
    migration_prev_res_in_sunbelt = db.Column("migration prev res in sunbelt", db.VARCHAR(1000))
    num_persons_worked_for_employer = db.Column("num persons worked for employer", db.VARCHAR(1000))
    family_members_under_118 = db.Column("family members under 118", db.VARCHAR(1000))
    father_birth_country = db.Column("father birth country", db.VARCHAR(1000))
    mother_birth_country = db.Column("mother birth country", db.VARCHAR(1000))
    birth_country = db.Column("birth country", db.VARCHAR(1000))
    citizenship = db.Column(db.VARCHAR(1000))
    own_business_or_self_employed = db.Column("own business or self employed", db.VARCHAR(1000))
    veterans_benefits = db.Column("veterans benefits", db.VARCHAR(1000))
    weeks_worked_in_year = db.Column("weeks worked in year", db.VARCHAR(1000))
    year = db.Column(db.VARCHAR(1000))
    salary_range = db.Column("salary range", db.VARCHAR(1000))
