package com.hospital.backend.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.hospital.backend.Model.PatientModel;
import com.hospital.backend.Repository.PatientRepository;

@RestController
@CrossOrigin("*")
public class PatientController {

    @Autowired
    private PatientRepository patientRepository;

    @PostMapping("/api/patient/add")
    public PatientModel addPatient(@RequestBody PatientModel pateintModel) {
        return patientRepository.save(pateintModel);
    }

    @GetMapping("/api/patient")
    public List<PatientModel> getPatient() {
        return patientRepository.findAll();
    }

    

}
