package com.hospital.backend.Repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.hospital.backend.Model.PatientModel;

public interface PatientRepository extends JpaRepository<PatientModel, Long>{
    
}
