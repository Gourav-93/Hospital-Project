package com.hospital.backend.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import java.util.List;

import com.hospital.backend.Model.DoctorModel;
import com.hospital.backend.Repository.DoctorRepository;

@RestController
@CrossOrigin(origins = "*")
public class DoctorController {

    @Autowired
    private DoctorRepository doctorRepository;

    @PostMapping("/api/doctor/add")
    public DoctorModel addDoctor(@RequestBody DoctorModel doctorModel) {
        return doctorRepository.save(doctorModel);
    }

    @GetMapping("/api/doctor")
    public List<DoctorModel> getDoctors() {
        return doctorRepository.findAll();
    }

    @DeleteMapping("/api/doctor/delete/{id}")
    public String deleteDoctor(@PathVariable Long id) {

        if (!doctorRepository.existsById(id)) {
            return "Doctor Not Found";
        }

        doctorRepository.deleteById(id);
        return "Doctor Deleted Successfully";
    }

}
