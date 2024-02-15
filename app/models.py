from django.db import models

# Create your models here.



class ODS_Licence(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    code_commune = models.CharField(max_length=500)
    commune = models.CharField(max_length=500)
    code_qpv = models.CharField(max_length=500)
    nom_qpv = models.CharField(max_length=500)
    departement = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    statut_geo = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    federation = models.CharField(max_length=500)
    f_1_4_ans = models.CharField(max_length=500)
    f_5_9_ans = models.CharField(max_length=500)
    f_10_14_ans = models.CharField(max_length=500)
    f_15_19_ans = models.CharField(max_length=500)
    f_20_24_ans = models.CharField(max_length=500)
    f_25_29_ans = models.CharField(max_length=500)
    f_30_34_ans = models.CharField(max_length=500)
    f_35_39_ans = models.CharField(max_length=500)
    f_40_44_ans = models.CharField(max_length=500)
    f_45_49_ans = models.CharField(max_length=500)
    f_50_54_ans = models.CharField(max_length=500)
    f_55_59_ans = models.CharField(max_length=500)
    f_60_64_ans = models.CharField(max_length=500)
    f_65_69_ans = models.CharField(max_length=500)
    f_70_74_ans = models.CharField(max_length=500)
    f_75_79_ans = models.CharField(max_length=500)
    f_80_99_ans = models.CharField(max_length=500)
    f_nr = models.CharField(max_length=500)
    h_1_4_ans = models.CharField(max_length=500)
    h_5_9_ans = models.CharField(max_length=500)
    h_10_14_ans = models.CharField(max_length=500)
    h_15_19_ans = models.CharField(max_length=500)
    h_20_24_ans = models.CharField(max_length=500)
    h_25_29_ans = models.CharField(max_length=500)
    h_30_34_ans = models.CharField(max_length=500)
    h_35_39_ans = models.CharField(max_length=500)
    h_40_44_ans = models.CharField(max_length=500)
    h_45_49_ans = models.CharField(max_length=500)
    h_50_54_ans = models.CharField(max_length=500)
    h_55_59_ans = models.CharField(max_length=500)
    h_60_64_ans = models.CharField(max_length=500)
    h_65_69_ans = models.CharField(max_length=500)
    h_70_74_ans = models.CharField(max_length=500)
    h_75_79_ans = models.CharField(max_length=500)
    h_80_99_ans = models.CharField(max_length=500)
    h_nr = models.CharField(max_length=500)
    nr_nr = models.CharField(max_length=500)
    total = models.CharField(max_length=500)
    file_name = models.CharField(max_length=500)
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.commune} - {self.nom_qpv} - {self.federation}"


class ODS_Club(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    code_commune = models.CharField(max_length=500)
    commune = models.CharField(max_length=500)
    code_qpv = models.CharField(max_length=500)
    nom_qpv = models.CharField(max_length=500)
    departement = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    statut_geo = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    federation = models.CharField(max_length=500)
    clubs = models.CharField(max_length=500)
    epa = models.CharField(max_length=500)
    total = models.CharField(max_length=500)
    file_name = models.CharField(max_length=500)
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.commune} - {self.nom_qpv} - {self.federation}"

  
class D_Sexe(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    code = models.CharField(max_length=1, primary_key=True)
    label = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.label}"


class D_Age_Group(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    code = models.CharField(max_length=15, primary_key=True)
    label = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.label}"


class D_Federation(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    code = models.CharField(max_length=3, primary_key=True)
    label = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.code} - {self.label}"


class D_Club_Type(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    code = models.CharField(max_length=3, primary_key=True)
    label = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.label}"


class D_Date(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    date = models.DateField(primary_key=True)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.year}"


class D_Geography(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    code = models.CharField(max_length=14, primary_key=True)
    code_commune = models.CharField(max_length=5)
    commune = models.CharField(max_length=150)
    code_qpv = models.CharField(max_length=8)
    qpv = models.CharField(max_length=150)
    code_departement = models.CharField(max_length=3)
    departement = models.CharField(max_length=150)
    region = models.CharField(max_length=100)
    statut = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.commune} - {self.qpv}"


class F_Licence(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    code = models.CharField(max_length=45, primary_key=True)
    nombre = models.IntegerField()
    federation_fk = models.ForeignKey(D_Federation, on_delete=models.CASCADE)
    sexe_fk = models.ForeignKey(D_Sexe, on_delete=models.CASCADE)
    age_group_fk = models.ForeignKey(D_Age_Group, on_delete=models.CASCADE)
    date_fk = models.ForeignKey(D_Date, on_delete=models.CASCADE)
    geography_fk = models.ForeignKey(D_Geography, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.federation_fk} - {self.sexe_fk} - {self.age_group_fk} - {self.geography_fk}"


class F_Club(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    code = models.CharField(max_length=30, primary_key=True)
    nombre = models.IntegerField()
    federation_fk = models.ForeignKey(D_Federation, on_delete=models.CASCADE)
    club_type_fk = models.ForeignKey(D_Club_Type, on_delete=models.CASCADE)
    date_fk = models.ForeignKey(D_Date, on_delete=models.CASCADE)
    geography_fk = models.ForeignKey(D_Geography, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.federation_fk} - {self.club_type_fk} - {self.geography_fk}"