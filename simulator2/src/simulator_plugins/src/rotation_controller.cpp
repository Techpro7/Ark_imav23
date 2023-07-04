#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>

namespace gazebo
{
  class RotationControllerPlugin : public ModelPlugin
  {
  public:
    void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
    {
      // Check if the model has a joint named "joint_name"
      physics::JointPtr joint = _model->GetJoint("rotation_joint");
      if (!joint)
      {
        gzerr << "Joint not found: joint_name" << std::endl;
        return;
      }

      // Apply effort to the joint to rotate the platform
      joint->SetForce(0, 10);
    }
  };

  GZ_REGISTER_MODEL_PLUGIN(RotationControllerPlugin)
}
