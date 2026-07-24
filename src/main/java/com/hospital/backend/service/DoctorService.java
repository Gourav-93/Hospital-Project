package com.hospital.backend.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.hospital.backend.model.DoctorModel;
import com.hospital.backend.repository.DoctorRepository;

import java.util.List;

@Service
public class DoctorService {

    @Autowired
    private DoctorRepository doctorRepository;

    public DoctorModel addDoctor(DoctorModel doctorModel) {
        return doctorRepository.save(doctorModel);
    }

    public List<DoctorModel> getDoctors() {
        return doctorRepository.findAll();
    }

    public boolean existsById(Long id) {
        return doctorRepository.existsById(id);
    }

    public void deleteDoctor(Long id) {
        doctorRepository.deleteById(id);
    }
}
