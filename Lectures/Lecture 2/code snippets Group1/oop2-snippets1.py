
# class HealthMinistry_boring:
#     def __init__(self):
#         self.hospitals = []


class HealthMinistry:
    def __init__(self, hospitals=None):
        # self.patients = []

        if hospitals is None:
            self.hospitals = []
        else:
            self.hospitals = hospitals

    def prettyprint(self):
        for h in self.hospitals:
            # print(h)
            h.prettyprint()


class Hospital:
    def __init__(self, hospital_id, name):
        self.hospital_id = hospital_id
        self.name = name
        self.patients = []

    def prettyprint(self):
        print(self.hospital_id, self.name)
        for p in self.patients:
            p.prettyprint()

    def __str__(self):
        return f"{self.hospital_id} {self.name} \n" + "\n".join([str(p) for p in self.patients])

    def __len__(self):
        return len(self.patients)


# stefansministry = HealthMinistry_boring()
# stefansministry.hospitals.append(Hospital(1, "Greys Anatomy"))

# anubhavsministry = HealthMinistry()


class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def prettyprint(self):
        print("\t", self.patient_id, self.name)

    def __str__(self):
        return f"{self.patient_id}  {self.name}"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        # short:
        # return self.name == other.name and self.patient_id == other.patient_id
        # try:
        # long:
        if self.name != other.name:
            return False

        if self.patient_id != other.patient_id:
            return False

        return True

        # except:
        #     return False


h1 = Hospital("h1", "Hospital 1")
p1 = Patient("p1", "Patient 1")
p2 = Patient("p2", "Patient 2")
h1.patients.append(p1)
h1.patients.append(p2)

h2 = Hospital("h2", "Hospital 2")
p3 = Patient("p3", "Patient 3")
p4 = Patient("p4", "Patient 4")
h2.patients.append(p3)
h2.patients.append(p4)


hm = HealthMinistry()
hm.hospitals.append(h1)
hm.hospitals.append(h2)


# for h in hm.hospitals:
#     for p in h.patients:
#         if p.name == "Patient 3":
#             print(p.name, "is in ", h.name)
#
#
# for p in hm.patients:
#     if p.name == "Patient 3":
#         print(p.name, "is in ", h.name)


# print(hm)
# hm.prettyprint()
#
# print(hm)

# print(p1)

print(h1)


print("Number of patients in h2", len(h2))


print(p1 == "hello world")

