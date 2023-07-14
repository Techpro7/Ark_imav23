// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: PoseStamped.proto

#include "PoseStamped.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/port.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// This is a temporary google only hack
#ifdef GOOGLE_PROTOBUF_ENFORCE_UNIQUENESS
#include "third_party/protobuf/version.h"
#endif
// @@protoc_insertion_point(includes)

namespace protobuf_Header_2eproto {
extern PROTOBUF_INTERNAL_EXPORT_protobuf_Header_2eproto ::google::protobuf::internal::SCCInfo<1> scc_info_Header;
}  // namespace protobuf_Header_2eproto
namespace protobuf_pose_2eproto {
extern PROTOBUF_INTERNAL_EXPORT_protobuf_pose_2eproto ::google::protobuf::internal::SCCInfo<2> scc_info_Pose;
}  // namespace protobuf_pose_2eproto
namespace gz_geometry_msgs {
class PoseStampedDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<PoseStamped>
      _instance;
} _PoseStamped_default_instance_;
}  // namespace gz_geometry_msgs
namespace protobuf_PoseStamped_2eproto {
static void InitDefaultsPoseStamped() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::gz_geometry_msgs::_PoseStamped_default_instance_;
    new (ptr) ::gz_geometry_msgs::PoseStamped();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::gz_geometry_msgs::PoseStamped::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<2> scc_info_PoseStamped =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 2, InitDefaultsPoseStamped}, {
      &protobuf_Header_2eproto::scc_info_Header.base,
      &protobuf_pose_2eproto::scc_info_Pose.base,}};

void InitDefaults() {
  ::google::protobuf::internal::InitSCC(&scc_info_PoseStamped.base);
}

::google::protobuf::Metadata file_level_metadata[1];

const ::google::protobuf::uint32 TableStruct::offsets[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::gz_geometry_msgs::PoseStamped, _has_bits_),
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::gz_geometry_msgs::PoseStamped, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::gz_geometry_msgs::PoseStamped, header_),
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::gz_geometry_msgs::PoseStamped, pose_),
  0,
  1,
};
static const ::google::protobuf::internal::MigrationSchema schemas[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  { 0, 7, sizeof(::gz_geometry_msgs::PoseStamped)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::gz_geometry_msgs::_PoseStamped_default_instance_),
};

void protobuf_AssignDescriptors() {
  AddDescriptors();
  AssignDescriptors(
      "PoseStamped.proto", schemas, file_default_instances, TableStruct::offsets,
      file_level_metadata, NULL, NULL);
}

void protobuf_AssignDescriptorsOnce() {
  static ::google::protobuf::internal::once_flag once;
  ::google::protobuf::internal::call_once(once, protobuf_AssignDescriptors);
}

void protobuf_RegisterTypes(const ::std::string&) GOOGLE_PROTOBUF_ATTRIBUTE_COLD;
void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::internal::RegisterAllTypes(file_level_metadata, 1);
}

void AddDescriptorsImpl() {
  InitDefaults();
  static const char descriptor[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
      "\n\021PoseStamped.proto\022\020gz_geometry_msgs\032\014H"
      "eader.proto\032\npose.proto\"S\n\013PoseStamped\022#"
      "\n\006header\030\001 \002(\0132\023.gz_std_msgs.Header\022\037\n\004p"
      "ose\030\002 \002(\0132\021.gazebo.msgs.Pose"
  };
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
      descriptor, 148);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "PoseStamped.proto", &protobuf_RegisterTypes);
  ::protobuf_Header_2eproto::AddDescriptors();
  ::protobuf_pose_2eproto::AddDescriptors();
}

void AddDescriptors() {
  static ::google::protobuf::internal::once_flag once;
  ::google::protobuf::internal::call_once(once, AddDescriptorsImpl);
}
// Force AddDescriptors() to be called at dynamic initialization time.
struct StaticDescriptorInitializer {
  StaticDescriptorInitializer() {
    AddDescriptors();
  }
} static_descriptor_initializer;
}  // namespace protobuf_PoseStamped_2eproto
namespace gz_geometry_msgs {

// ===================================================================

void PoseStamped::InitAsDefaultInstance() {
  ::gz_geometry_msgs::_PoseStamped_default_instance_._instance.get_mutable()->header_ = const_cast< ::gz_std_msgs::Header*>(
      ::gz_std_msgs::Header::internal_default_instance());
  ::gz_geometry_msgs::_PoseStamped_default_instance_._instance.get_mutable()->pose_ = const_cast< ::gazebo::msgs::Pose*>(
      ::gazebo::msgs::Pose::internal_default_instance());
}
void PoseStamped::clear_header() {
  if (header_ != NULL) header_->Clear();
  clear_has_header();
}
void PoseStamped::clear_pose() {
  if (pose_ != NULL) pose_->Clear();
  clear_has_pose();
}
#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int PoseStamped::kHeaderFieldNumber;
const int PoseStamped::kPoseFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

PoseStamped::PoseStamped()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  ::google::protobuf::internal::InitSCC(
      &protobuf_PoseStamped_2eproto::scc_info_PoseStamped.base);
  SharedCtor();
  // @@protoc_insertion_point(constructor:gz_geometry_msgs.PoseStamped)
}
PoseStamped::PoseStamped(const PoseStamped& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(NULL),
      _has_bits_(from._has_bits_) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  if (from.has_header()) {
    header_ = new ::gz_std_msgs::Header(*from.header_);
  } else {
    header_ = NULL;
  }
  if (from.has_pose()) {
    pose_ = new ::gazebo::msgs::Pose(*from.pose_);
  } else {
    pose_ = NULL;
  }
  // @@protoc_insertion_point(copy_constructor:gz_geometry_msgs.PoseStamped)
}

void PoseStamped::SharedCtor() {
  ::memset(&header_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&pose_) -
      reinterpret_cast<char*>(&header_)) + sizeof(pose_));
}

PoseStamped::~PoseStamped() {
  // @@protoc_insertion_point(destructor:gz_geometry_msgs.PoseStamped)
  SharedDtor();
}

void PoseStamped::SharedDtor() {
  if (this != internal_default_instance()) delete header_;
  if (this != internal_default_instance()) delete pose_;
}

void PoseStamped::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const ::google::protobuf::Descriptor* PoseStamped::descriptor() {
  ::protobuf_PoseStamped_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_PoseStamped_2eproto::file_level_metadata[kIndexInFileMessages].descriptor;
}

const PoseStamped& PoseStamped::default_instance() {
  ::google::protobuf::internal::InitSCC(&protobuf_PoseStamped_2eproto::scc_info_PoseStamped.base);
  return *internal_default_instance();
}


void PoseStamped::Clear() {
// @@protoc_insertion_point(message_clear_start:gz_geometry_msgs.PoseStamped)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  cached_has_bits = _has_bits_[0];
  if (cached_has_bits & 3u) {
    if (cached_has_bits & 0x00000001u) {
      GOOGLE_DCHECK(header_ != NULL);
      header_->Clear();
    }
    if (cached_has_bits & 0x00000002u) {
      GOOGLE_DCHECK(pose_ != NULL);
      pose_->Clear();
    }
  }
  _has_bits_.Clear();
  _internal_metadata_.Clear();
}

bool PoseStamped::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:gz_geometry_msgs.PoseStamped)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // required .gz_std_msgs.Header header = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(10u /* 10 & 0xFF */)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessage(
               input, mutable_header()));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // required .gazebo.msgs.Pose pose = 2;
      case 2: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(18u /* 18 & 0xFF */)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessage(
               input, mutable_pose()));
        } else {
          goto handle_unusual;
        }
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, _internal_metadata_.mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:gz_geometry_msgs.PoseStamped)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:gz_geometry_msgs.PoseStamped)
  return false;
#undef DO_
}

void PoseStamped::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:gz_geometry_msgs.PoseStamped)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  cached_has_bits = _has_bits_[0];
  // required .gz_std_msgs.Header header = 1;
  if (cached_has_bits & 0x00000001u) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      1, this->_internal_header(), output);
  }

  // required .gazebo.msgs.Pose pose = 2;
  if (cached_has_bits & 0x00000002u) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      2, this->_internal_pose(), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        _internal_metadata_.unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:gz_geometry_msgs.PoseStamped)
}

::google::protobuf::uint8* PoseStamped::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  (void)deterministic; // Unused
  // @@protoc_insertion_point(serialize_to_array_start:gz_geometry_msgs.PoseStamped)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  cached_has_bits = _has_bits_[0];
  // required .gz_std_msgs.Header header = 1;
  if (cached_has_bits & 0x00000001u) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageToArray(
        1, this->_internal_header(), deterministic, target);
  }

  // required .gazebo.msgs.Pose pose = 2;
  if (cached_has_bits & 0x00000002u) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageToArray(
        2, this->_internal_pose(), deterministic, target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:gz_geometry_msgs.PoseStamped)
  return target;
}

size_t PoseStamped::RequiredFieldsByteSizeFallback() const {
// @@protoc_insertion_point(required_fields_byte_size_fallback_start:gz_geometry_msgs.PoseStamped)
  size_t total_size = 0;

  if (has_header()) {
    // required .gz_std_msgs.Header header = 1;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSize(
        *header_);
  }

  if (has_pose()) {
    // required .gazebo.msgs.Pose pose = 2;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSize(
        *pose_);
  }

  return total_size;
}
size_t PoseStamped::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:gz_geometry_msgs.PoseStamped)
  size_t total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        _internal_metadata_.unknown_fields());
  }
  if (((_has_bits_[0] & 0x00000003) ^ 0x00000003) == 0) {  // All required fields are present.
    // required .gz_std_msgs.Header header = 1;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSize(
        *header_);

    // required .gazebo.msgs.Pose pose = 2;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSize(
        *pose_);

  } else {
    total_size += RequiredFieldsByteSizeFallback();
  }
  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void PoseStamped::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:gz_geometry_msgs.PoseStamped)
  GOOGLE_DCHECK_NE(&from, this);
  const PoseStamped* source =
      ::google::protobuf::internal::DynamicCastToGenerated<const PoseStamped>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:gz_geometry_msgs.PoseStamped)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:gz_geometry_msgs.PoseStamped)
    MergeFrom(*source);
  }
}

void PoseStamped::MergeFrom(const PoseStamped& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:gz_geometry_msgs.PoseStamped)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  cached_has_bits = from._has_bits_[0];
  if (cached_has_bits & 3u) {
    if (cached_has_bits & 0x00000001u) {
      mutable_header()->::gz_std_msgs::Header::MergeFrom(from.header());
    }
    if (cached_has_bits & 0x00000002u) {
      mutable_pose()->::gazebo::msgs::Pose::MergeFrom(from.pose());
    }
  }
}

void PoseStamped::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:gz_geometry_msgs.PoseStamped)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void PoseStamped::CopyFrom(const PoseStamped& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:gz_geometry_msgs.PoseStamped)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool PoseStamped::IsInitialized() const {
  if ((_has_bits_[0] & 0x00000003) != 0x00000003) return false;
  if (has_header()) {
    if (!this->header_->IsInitialized()) return false;
  }
  if (has_pose()) {
    if (!this->pose_->IsInitialized()) return false;
  }
  return true;
}

void PoseStamped::Swap(PoseStamped* other) {
  if (other == this) return;
  InternalSwap(other);
}
void PoseStamped::InternalSwap(PoseStamped* other) {
  using std::swap;
  swap(header_, other->header_);
  swap(pose_, other->pose_);
  swap(_has_bits_[0], other->_has_bits_[0]);
  _internal_metadata_.Swap(&other->_internal_metadata_);
}

::google::protobuf::Metadata PoseStamped::GetMetadata() const {
  protobuf_PoseStamped_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_PoseStamped_2eproto::file_level_metadata[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace gz_geometry_msgs
namespace google {
namespace protobuf {
template<> GOOGLE_PROTOBUF_ATTRIBUTE_NOINLINE ::gz_geometry_msgs::PoseStamped* Arena::CreateMaybeMessage< ::gz_geometry_msgs::PoseStamped >(Arena* arena) {
  return Arena::CreateInternal< ::gz_geometry_msgs::PoseStamped >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)
