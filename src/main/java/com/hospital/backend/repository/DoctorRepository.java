package com.hospital.backend.repository;



import org.springframework.data.jpa.repository.JpaRepository;
import com.hospital.backend.model.DoctorModel;


public interface DoctorRepository extends JpaRepository<DoctorModel, Long>{
    
}
